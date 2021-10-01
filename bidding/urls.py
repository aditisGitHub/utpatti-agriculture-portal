from django.urls import path
from . import views

urlpatterns = [
    path('farmer/<int:fid>/', views.farmerPro, name='farmerPage'),
    path('farmer/<int:fid>/<str:cid>/', views.createBid, name = 'createBid'),
    path('farmer/<int:fid>/<str:cid>/success', views.bid_success, name = 'successBid'),
    path('merchant/<int:mid>/bid/<str:bViewed>', views.viewBid, name = 'viewBid'),
    path('merchant/<int:mid>', views.merchantPro, name='merchantPage'),
    ]