from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from apps.deals.models import Deals


@extend_schema(tags=["deals"])
class DealsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = (DjangoFilterBackend,)
    queryset = Deals.objects.all()
    # serializer_class = DealsSerializer
