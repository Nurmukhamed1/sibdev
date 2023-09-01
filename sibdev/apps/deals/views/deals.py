from django.db.models import Sum
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
        queryset = queryset.values('customer').annotate(spent_money=Sum('total')).order_by('-spent_money')[:5]
        serializer = self.get_serializer(queryset, many=True)
        return Response({"response": serializer.data})
