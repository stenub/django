from django.forms import modelform_factory, forms, TextInput, PasswordInput, Select, ChoiceField

from django import forms

from .models import Device, Customer

from django_celery_beat.models import CrontabSchedule

from django.utils.translation import gettext_lazy as _


class customer_new_form(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'number', 'comment']
        labels = {
            'name': _(''),
            'number': _(''),
            'comment': _(''),
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Name'}),
            'number': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Number'}),
            'comment': TextInput(attrs={'class': 'form-control mb-2 mr-lg-2', 'placeholder': 'Comment'}),
        }



class device_new_form(forms.ModelForm):

    class Meta:
        model = Device
        fields = ['customer', 'hostname', 'mgt_ip', 'username', 'password']
        labels = {
            'customer': _(''),
            'hostname': _(''),
            'mgt_ip': _(''),
            'username': _(''),
            'password': _(''),
        }
        widgets = {
            'customer': Select(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Customer'}),
            'hostname': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Hostname'}),
            'mgt_ip': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Management IP'}),
            'username': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Password'}),
        }



class schedule_new_form(forms.ModelForm):


    class Meta:

        def bereich(x):
            y = [('*', '*')]
            for i in range(1, x+1):
                j = str(i)
                z = (i, j)
                y.append(z)
                #print(y)
            return y


        model = CrontabSchedule
        fields = ['minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year']
        labels = {
            'minute':_(''),
            'hour':_(''),
            'day_of_week':_(''),
            'day_of_month':_(''),
            'month_of_year':_(''),
        }
        widgets = {
            'minute': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}, choices=bereich(60)),
            'hour': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}, choices=bereich(24)),
            'day_of_week': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}, choices=bereich(7)),
            'day_of_month': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}, choices=bereich(30)),
            'month_of_year': Select(attrs={'class': 'form-control mb-2 mr-sm-2'}, choices=bereich(12)),
        }
