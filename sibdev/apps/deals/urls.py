from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.deals.views import DealsViewSet

router = DefaultRouter()
router.register("", DealsViewSet, basename="deals")

urlpatterns = [
    path("", include(router.urls)),
]
