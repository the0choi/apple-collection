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
  path('devices/<int:device_id>/remove_version/<int:version_id>/', views.remove_version, name='remove_version'),
  path('devices/<int:device_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
  path('devices/<int:device_id>/remove_accessory/<int:accessory_id>/', views.remove_accessory, name='remove_accessory'),
  path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]