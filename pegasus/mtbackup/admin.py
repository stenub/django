from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Device, Customer, User

admin.site.register(Device)
admin.site.register(Customer)
admin.site.register(User, UserAdmin)
