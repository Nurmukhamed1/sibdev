from django.db.models import Sum, Count
from rest_framework import serializers

from apps.deals.models import Deals


class DealsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="customer")
    spent_money = serializers.IntegerField()
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Deals
        fields = (
            "username",
            "spent_money",
            "gems",
        )

    def get_gems(self, obj):
        queryset = Deals.objects.all()
        top_clients = queryset.values('customer').annotate(spent_money=Sum('total')).order_by('-spent_money')[:5]

        gems_of_top_clients = (
            queryset.filter(customer__in=top_clients.values_list('customer', flat=True))
            .values('item').
            annotate(customer_count=Count('customer', distinct=True))
            .filter(customer_count__gte=2)
        )

        return (queryset.filter(customer=obj["customer"]).
                filter(item__in=gems_of_top_clients.values_list("item", flat=True))
                .distinct('item').
                values_list("item", flat=True))
