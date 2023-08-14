from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('devices/', views.devices_index, name='index'),
  path('devices/<int:device_id>/', views.devices_detail, name='detail'),
  path('devices/create/', views.DeviceCreate.as_view(), name='devices_create'),
  path('devices/<int:pk>/update/', views.DeviceUpdate.as_view(), name='devices_update'),
  path('devices/<int:pk>/delete/', views.DeviceDelete.as_view(), name='devices_delete'),
  path('devices/<int:device_id>/add_version/', views.add_version, name='add_version'),
]