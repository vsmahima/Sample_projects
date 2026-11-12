from django.db import models

# Create your models here.
class AssetRegistration(models.Model):
    assetId=models.CharField(max_length=10)
    asset_name=models.CharField(max_length=50)
    category=models.CharField(max_length=30)
    purchase_date=models.DateField()
    purchase_cost=models.FloatField()
    supplier_name=models.CharField(max_length=80)
    asset_location=models.CharField(max_length=50)
    asset_condition=models.CharField(max_length=15)
    asset_status=models.CharField(max_length=15)
    asset_description=models.TextField(max_length=250)
