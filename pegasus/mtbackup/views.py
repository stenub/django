from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import new_DeviceForm


def index(request):
    return HttpResponse("Hello World. Du bist im mtbackup index.")

def get_backup(request):
    return HttpResponse("Das ist der get_backup view.")

def new_device(request):
    form = new_DeviceForm()
    return render(request, 'mtbackup/new_device.html', {'form': form})
