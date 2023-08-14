from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class DeviceCreate(CreateView):
    model = Device
    fields = '__all__'


class DeviceUpdate(UpdateView):
    model = Device
    fields = ['release_year', 'category', 'colours']


class DeviceDelete(DeleteView):
    model = Device
    success_url = '/devices'
