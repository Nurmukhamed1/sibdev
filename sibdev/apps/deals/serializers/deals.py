from rest_framework import serializers

from apps.deals.models import Deals


class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = (
            "customer",
            "item",
            "total",
            "quantity",
            "date",
        )
