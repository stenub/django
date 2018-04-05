from django.db import models

# Create your models here.

class Device(models.Model):
    hostname = models.CharField(max_length=50)
    mgt_ip = models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
    username = models.CharField(max_length=50, default='admin')
    password = models.CharField(max_length=50, default='', blank=True)
    def __str__(self):
        return self.hostname
