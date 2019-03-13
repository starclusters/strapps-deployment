from django.db import models
from datetime import datetime

# Create your models here.
class Biditem(models.Model):
    payitem_number = models.CharField(max_length=100)
    payitem_desc = models.CharField(max_length=150)
    unit = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=12, decimal_places=3, null=True)
    county = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    item = models.CharField(max_length=50)
    awarded_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    letting_date=models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.payitem_number
