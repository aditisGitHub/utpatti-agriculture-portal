from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Farmer, Bid, Crop, BidEntry, Merchant
from .forms import CreateBidForm, AddBid

def farmerPro(request, fid):
    fp = Farmer.objects.get(adhr_no=fid)
    fc = Crop.objects.filter(grown_by=fp)
    return render(request, 'bidding/farmer-page.html',  {
        'farmerPage': fp,
        'farmCrops': fc
    })

def merchantPro(request, mid):
    curr_merchant = mid
    all_bids = Bid.objects.filter(is_Active = True)
    crops_all_bids = Crop.objects.filter(bid_for_crop__in=all_bids).values('crop_name', 'qty_grown', 'crop_type', 'grown_by', 'bid_for_crop')
    #all_entries = BidEntry.objects.all()
    return render(request, 'bidding/merchant-page.html', {
        'active_bids': all_bids,    
        'active_bids_crops': crops_all_bids,
        #'all_entries': all_entries 
        'curr_m': curr_merchant        
    })

def createBid(request, fid, cid):
    crop_selected = Crop.objects.get(crop_id=cid)
    by_farmer = Farmer.objects.get(adhr_no=fid)
    
    try:

        if request.method == 'POST':
            bid_form = CreateBidForm(request.POST)
            if bid_form.is_valid():
                #Fetching cleaned values from form
                b1 = bid_form.cleaned_data['b_id']
                b2 = bid_form.cleaned_data['b_start']
                b3 = bid_form.cleaned_data['b_end']
                b4 = bid_form.cleaned_data['b_price']
                #Saving to db
                new_bid, isNew = Bid.objects.update_or_create(bid_id=b1, bid_start_date=b2, bid_close_date=b3, base_price=b4)
                if (isNew):
                    Crop.objects.filter(crop_id = cid).update(bid_for_crop = new_bid)
                return redirect("https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views")

        else:
            bid_form = CreateBidForm()
        
        return render(request, 'bidding/bid_create.html', {
            'farmerPage': by_farmer,
            'farmCrops': crop_selected,
            'create_bid_form': bid_form
        })

    except Exception as ex:
        return redirect("https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/")

def viewBid(request, mid, bViewed):
    m_id = Merchant.objects.get(adhr_no=mid)
    bid_selected = Bid.objects.get(bid_id = bViewed)
    all_entries = BidEntry.objects.filter(bid=bViewed)
    try: 
        if request.method =='POST':
            new_bid_price = AddBid(request.POST)
           
            if new_bid_price.is_valid():
                bp = new_bid_price.cleaned_data['b_amt']
                
                new_bidEntry = BidEntry.objects.create( bid = bid_selected, merchant_bidding = m_id, bid_price = bp)
                print(new_bidEntry)

                return redirect ("https://docs.djangoproject.com/en/dev/ref/forms/widgets/")
        else: 
            new_bid_price = AddBid()
            return render(request, 'bidding/bid_view.html', {
                    'curr_merchant': m_id,
                    'selected_bid': bid_selected,
                    'bid_status': all_entries,
                    'bid_entry_form': new_bid_price
        }) 

    except Exception as exc:     
        print(exc)
        return HttpResponse("ju")

def bid_success(request, fid, cid):
    return render(request, 'bidding/success.html', {
        'f_id': fid,
        'c_id': cid
    })