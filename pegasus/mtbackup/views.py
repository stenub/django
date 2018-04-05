from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import new_DeviceForm

from .models import Device

from .tasks import create_backup

def index(request):
    return HttpResponse("Hello World. Du bist im mtbackup index.")

def get_backup(request):
    devices = Device.objects.all()
    for d in devices:
        create_backup.delay(d.mgt_ip, 22, d.username, d.password)
        
    return HttpResponse("get_backup")

def new_device(request):
    if request.method == 'GET':
        form = new_DeviceForm()
    elif request.method == 'POST':
        form = new_DeviceForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            return HttpResponse("Speichern erfolgreich!")
    return render(request, 'mtbackup/new_device.html', {'form': form})        
        

def show_device(request):
    devices = Device.objects.all()
    return HttpResponse("show_device")
