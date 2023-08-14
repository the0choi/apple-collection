from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('devices/', views.devices_index, name='index'),
  path('devices/<int:device_id>/', views.devices_detail, name='detail'),
]