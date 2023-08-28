from django.db import models


class Deals(models.Model):
    customer = models.CharField(max_length=300)
    item = models.CharField(max_length=300)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
