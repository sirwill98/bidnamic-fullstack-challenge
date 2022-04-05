from django.urls import path, re_path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('log-out', views.logout, name='log-out'),
    path('view-bids', views.view_bids, name='view-bids'),
    path('create-bid', views.multi_stage_bid_form, name='create-bid')
    ]