from rest_framework import views
from rest_framework.parsers import FileUploadParser

from apps.deals.serializers import FileUploadSerializer


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            uploaded_file = serializer.validated_data["deals"]
