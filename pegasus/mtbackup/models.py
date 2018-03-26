from django.db import models

# Create your models here.

class Device(models.Model):
    hostname = models.CharField(max_length=50)
    mgt_ip = models.GenericIPAddressField()
    username = models.CharField(max_length=50, default='admin')
    password = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.hostname
