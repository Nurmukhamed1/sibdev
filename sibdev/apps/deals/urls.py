from django.urls import path
from apps.deals.views import DealsViewSet, FileUploadView

urlpatterns = [
    path("list/", DealsViewSet.as_view({"get": "list"}), name="deals"),
    path("upload/", FileUploadView.as_view(), name="upload"),
]
