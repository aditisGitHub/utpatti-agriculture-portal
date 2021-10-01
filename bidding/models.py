from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from datetime import date

class Farmer(models.Model):
    adhr_no = models.IntegerField(primary_key=True)
    farm_exp = models.IntegerField(null=False, default=0)
    
class Merchant(models.Model):
    adhr_no = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=50)

    
class Bid(models.Model):
    bid_id = models.CharField(primary_key=True, max_length=10)
    bid_start_date = models.DateField(blank=False, default=date.today)
    bid_close_date = models.DateField(blank=False, default=date.today)
    base_price = models.FloatField(blank=False, default=0.0)
    is_Active = models.BooleanField(default=True)


class Crop(models.Model):
    crop_id = models.CharField(primary_key=True, max_length=10)
    crop_name = models.CharField(max_length=100, null=True)
    class Seasons(models.TextChoices):
        RABI = 'Rabi'
        KHARIF = 'Kharif'

    season = models.CharField(choices=Seasons.choices, max_length=15)
    qty_grown = models.FloatField(null=False, default=0.0)
    in_stock = models.BooleanField(default=True)
    crop_type = models.CharField(max_length=30, blank=False)
    qty_predicted = models.FloatField(blank=False, default=0.0)
    grown_by = models.ForeignKey(Farmer, on_delete=CASCADE)
    bid_for_crop = models.OneToOneField(Bid, on_delete=models.PROTECT, null=True, blank=True)

class BidEntry(models.Model):
    bid = models.ForeignKey(Bid, on_delete=CASCADE)
    merchant_bidding = models.ForeignKey(Merchant, on_delete=CASCADE)
    bid_price = models.FloatField(default=0.0)
    bid_time = models.DateTimeField(auto_now=True)




