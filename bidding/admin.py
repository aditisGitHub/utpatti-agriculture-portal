from django.contrib import admin
from .models import Farmer, Merchant, Crop, Bid, BidEntry

admin.site.register(Farmer)
admin.site.register(Merchant)
admin.site.register(Crop)
admin.site.register(Bid)
admin.site.register(BidEntry)
