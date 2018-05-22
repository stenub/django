from django.contrib import admin

# Register your models here.

from .models import Device, Customer

admin.site.register(Device)
admin.site.register(Customer)
