from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from .models import Device, Customer

from django_celery_beat.models import CrontabSchedule

from .forms import customer_new_form, device_new_form, schedule_new_form

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .tasks import *

from celery import chord


def dashboard(request):
    return render(request, 'mtbackup/dashboard.html')


def index(request):
    return HttpResponse("Hello World. Du bist im mtbackup index")


def customer_list(request):
    customers_all = Customer.objects.all()
    paginator = Paginator(customers_all, 10)

    page = request.GET.get('page', 1)


    if request.method == "POST" and 'action' in request.POST:
        if request.POST.get('action') == 'delete':
            customers_to_delete = request.POST.getlist('select')
            # customers_to_delete.delete()
            print("Customers to delete", customers_to_delete)
            return redirect(customer_list)


    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)


    return render(request, 'mtbackup/customer_list.html', {'customers': customers })


def customer_new(request):
    if request.method == "GET":
        form = customer_new_form()
    if request.method == "POST":
        #print("POST erhalten")
        form = customer_new_form(request.POST)
        if form.is_valid():
            form.save()
            #print("Speichern erfogreich!")
            return redirect(customer_list)
        else:
            print("Fehler")
    return render(request, 'mtbackup/customer_new.html', {'form': form})



def device_list(request):
    devices_all = Device.objects.all()
    paginator = Paginator(devices_all, 10)

    page = request.GET.get('page', 1)


    if request.method == "POST" and 'action' in request.POST:
        if request.POST.get('action') == 'backup':
            device_selections = request.POST.getlist('select')
            #print(device_selections)

            dev_objects = Device.objects.filter(id__in=device_selections)
            #print(dev_objects)

            for dev in dev_objects:
                create_backup.delay(dev.customer.number, dev.hostname, dev.mgt_ip, 22, dev.username, dev.password)

            #chord(backup_test.s(dev.hostname, dev.mgt_ip, dev.username, dev.password)for dev in dev_objects)(test_print.s())


            #print(request.POST)

        elif request.POST.get('action') == 'delete':
            devices_to_delete = request.POST.getlist('select')
            # devices_to_delete.delete()
            print("Devices to delete", devices_to_delete)
        return redirect(device_list)


    try:
        devices = paginator.page(page)
    except PageNotAnInteger:
        devices = paginator.page(1)
    except EmptyPage:
        devices = paginator.page(paginator.num_pages)


    return render(request, 'mtbackup/device_list.html', {'devices': devices })





def device_new(request):
    if request.method == "GET":
        form = device_new_form()
    if request.method == "POST":
        #print("POST erhalten")
        form = device_new_form(request.POST)
        if form.is_valid():
            form.save()
            #print("Speichern erfogreich!")
            return redirect(device_list)
        else:
            print("Fehler")
    return render(request, 'mtbackup/device_new.html', {'form': form})


#def device_delete(request, slug):
#    device_to_delete = device.objects.filter(slug=slug)
#    device_to_delete.delete()
#    return redirect(device_list)


def schedule_list(request):
    schedules = CrontabSchedule.objects.all()
    return render(request, 'mtbackup/schedule_list.html', {'schedules': schedules})

def schedule_new(request):
    if request.method == "GET":
        form = schedule_new_form()
    if request.method == "POST":
        form = schedule_new_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(schedule_new)
    return render(request, 'mtbackup/schedule_new.html', {'form':form})


def base(request):
    return render(request, 'mtbackup/base.html', {})



