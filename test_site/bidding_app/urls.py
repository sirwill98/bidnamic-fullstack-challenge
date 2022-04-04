from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('clientSignup', views.clientSignup, name='clientSignup'),
    path('', views.index, name='index')
    ]