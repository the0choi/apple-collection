from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import VersionForm
from .models import Device


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
    return render(request, 'devices/detail.html', {
        'device': device, 'version_form': version_form
    })


class DeviceCreate(CreateView):
    model = Device
    fields = '__all__'


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
