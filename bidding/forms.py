from django.db.models import fields
from bidding.models import Bid
from django import forms
from .models import Bid, BidEntry

class CreateBidForm(forms.Form):
    b_id = forms.CharField(required=True, label="Bid Id")
    b_start = forms.DateField(label="Bid Start Date")
    b_end = forms.DateField(label="Bid End Date")
    b_price = forms.FloatField(label="Base Price")

class AddBid(forms.Form):
    b_amt = forms.FloatField(required=True, 
                             widget=forms.TextInput(attrs={'placeholder': 'Bid Price'}))    