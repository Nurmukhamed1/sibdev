from django.db.models import Sum, Count
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from apps.deals.models import Deals
from apps.deals.serializers import DealsSerializer


@extend_schema(tags=["deals"])
class DealsViewSet(viewsets.GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = Deals.objects.all()

    serializer_class = DealsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        top_clients = queryset.values('customer').annotate(spent_money=Sum('total')).order_by('-spent_money')[:5]
        gems_of_top_clients = (
            queryset.filter(customer__in=top_clients.values_list('customer', flat=True))
            .values('item').
            annotate(customer_count=Count('customer', distinct=True))
            .filter(customer_count__gte=2)
        )

        client_data = []
        for client in top_clients:
            obj = {
                "username": client["customer"],
                "spent_money": client["spent_money"],
                "gems": [],
            }
            gems = queryset.filter(customer=client['customer']).filter(
                item__in=gems_of_top_clients.values_list("item", flat=True)).distinct('item')
            for gem in gems:
                obj['gems'].append(gem.item)
            client_data.append(obj)
        serializer = self.get_serializer(client_data, many=True)
        return Response({"response": serializer.data})
