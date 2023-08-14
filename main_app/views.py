from django.shortcuts import render

from .models import Device


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def devices_index(request):
    devices = Device.objects.all()
    return render(request, 'devices/index.html', {
        'devices': devices
    }
    )


def devices_detail(request, device_id):
    device = Device.objects.get(id=device_id)
    return render(request, 'devices/detail.html', {'device': device})
