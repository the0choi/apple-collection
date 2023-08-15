from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import VersionForm
from .models import Device, Accessory, Version


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def devices_index(request):
    devices = Device.objects.all()
    return render(request, 'devices/index.html', {
        'devices': devices
    })


def devices_detail(request, device_id):
    device = Device.objects.get(id=device_id)
    version_form = VersionForm()
    id_list = device.accessories.all().values_list('id')
    accessories_device_doesnt_have = Accessory.objects.exclude(id__in=id_list)
    return render(request, 'devices/detail.html', {
        'device': device, 'version_form': version_form, 'accessories': accessories_device_doesnt_have
    })


class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'release_year', 'type', 'operating_system']


class DeviceUpdate(UpdateView):
    model = Device
    fields = ['release_year', 'type', 'operating_system']


class DeviceDelete(DeleteView):
    model = Device
    success_url = '/devices'


def add_version(request, device_id):
    form = VersionForm(request.POST)
    if form.is_valid():
        new_version = form.save(commit=False)
        new_version.device_id = device_id
        new_version.save()
    return redirect('detail', device_id=device_id)

def remove_version(request, device_id, version_id):
    version = Version.objects.get(id=version_id).delete()
    return redirect('detail', device_id=device_id)

class AccessoryList(ListView):
    model = Accessory


class AccessoryDetail(DetailView):
    model = Accessory


class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'


class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['name', 'description']


class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories'


def assoc_accessory(request, device_id, accessory_id):
    Device.objects.get(id=device_id).accessories.add(accessory_id)
    return redirect('detail', device_id=device_id)

def remove_accessory(request, device_id, accessory_id):
    Device.objects.get(id=device_id).accessories.remove(accessory_id)
    return redirect('detail', device_id=device_id)
