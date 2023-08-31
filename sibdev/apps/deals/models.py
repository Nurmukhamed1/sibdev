from django.db import models
from import_export import resources


class Deals(models.Model):
    customer = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class DealsResource(resources.ModelResource):
    class Meta:
        model = Deals
        # import_id_fields = [""]
        skip_unchanged = True
        use_bulk = True
