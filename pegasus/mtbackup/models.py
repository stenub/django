from django.db import models
from django_celery_beat.models import CrontabSchedule


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=6)
    comment = models.CharField(max_length=150, default='', blank=True)

    def __str__(self):
        return (str(self.number) + '-' + self.name)

    class Meta:
        ordering = ['number']


class Device(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=50)
    mgt_ip = models.GenericIPAddressField(protocol='IPv4')
    mgt_port = models.IntegerField(default=22)
    username = models.CharField(max_length=50,)
    password = models.CharField(max_length=50, default='', blank=True)
    description = models.CharField(max_length=100, default='', blank=True)


    def __str__(self):
        return self.hostname

    class Meta:
        ordering = ['hostname']


#TODO: Das Schedule Model lässt sich nicht mehr entfernen. Datenbank komplett löschen und neu aufbauen, dabei ein
#neues User Model anlegen, wenn benötigt. Anleitung: https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#extending-the-existing-user-model
class Schedule(CrontabSchedule):

    MINUTE_CHOICES = [
        ("*", '*'), (5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'),
        (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60')
    ]
#    minute = models.CharField(max_length=2, choices=MINUTE_CHOICES, default='*')



# Die Idee hier ist das CrontabSchedule model zu erweitern indem man davon erbt und auf Basis dessen
# dann (möglicherweise) ein neues Model erstellt, in dem zB noch eine Description enthalten ist.
# Irgendwo muss dann auch die zuordnung laufen zwischen crontabschedule und den backup tasks und devices.
# Es gibt eine tabelle in der datenbank die das möglicherweise schon tut. django_celery_beat_periodictask(s) ?
#
#
# redis ist der broker, dieser muss mit  ./redis-4.0.9/src/redis-server  gestartet werden
# celery ist der workerchef, dieser muss mit  celery -A pegasus worker -l info  gestartet werden wenn
# man sich im Verzeichnis  /Users/cosmic/Documents/django/pegasus  befindet.