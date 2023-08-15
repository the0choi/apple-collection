from django.contrib import admin

from .models import Device, Version, Accessory

admin.site.register(Device)
admin.site.register(Version)
admin.site.register(Accessory)