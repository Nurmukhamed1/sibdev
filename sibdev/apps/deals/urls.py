from django.urls import path
from apps.deals.views import DealsViewSet, UploadView

urlpatterns = [
    path("list/", DealsViewSet.as_view({"get": "list"}), name="deals"),
    path("upload/", UploadView.as_view(), name="upload"),
]
