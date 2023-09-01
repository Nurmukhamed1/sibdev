from rest_framework import serializers

from apps.deals.models import Deals


class DealsSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    spent_money = serializers.IntegerField()
    gems = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = Deals
        fields = (
            "username",
            "spent_money",
            "gems",
        )
