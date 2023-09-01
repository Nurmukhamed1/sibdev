from _decimal import InvalidOperation

import pandas as pd
from django.core.exceptions import ValidationError
# from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, parsers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from tablib import Dataset

from apps.deals.models import DealsResource


@extend_schema(tags=["upload deals"])
class UploadView(generics.GenericAPIView):
    parser_classes = (parsers.MultiPartParser,)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get("deals", None)
        if not file or not file.name.endswith('csv'):
            return Response(
                data={"status": "error", "desc": "Enter a csv formatted 'deals' file!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        df = pd.read_csv(file)
        deals_resource = DealsResource()
        dataset = Dataset().load(df)
        try:
            result = deals_resource.import_data(
                dataset,
                dry_run=True,
                raise_errors=True,
            )
        except InvalidOperation:
            return Response(
                data={"status": "error", "desc": "Data type is not correct"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError:
            return Response(
                data={"status": "error", "desc": "Data type is not correct"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not result.has_errors():
            deals_resource.import_data(dataset, dry_run=False)
            return Response({"status": "ok"})
        return Response(
            data={"status": "error"},
            status=status.HTTP_400_BAD_REQUEST,
        )
