from django.forms import modelform_factory, forms, TextInput, PasswordInput, Select

from django import forms

from .models import Device

from django_celery_beat.models import CrontabSchedule

from django.utils.translation import gettext_lazy as _

class device_new_form(forms.ModelForm):

    class Meta:
        model = Device
        fields = ['hostname', 'mgt_ip', 'username', 'password']
        labels = {
            'hostname': _(''),
            'mgt_ip': _(''),
            'username': _(''),
            'password': _(''),
        }
        widgets = {
            'hostname': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Hostname'}),
            'mgt_ip': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Management IP'}),
            'username': TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Password'}),
        }



class DeviceForm(forms.Form):
    devices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="Do something with this Device:")
    #your_name = forms.CharField(label="Your Name", max_length=100)



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



#device_new_form = modelform_factory(device, fields=('hostname','mgt_ip','username','password'))

#class device_new_form(forms.Form):

#    hostname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder':'Hostname'}), max_length=50, label="")
#    mgt_ip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder':'Management IP'}), max_length=50, label="")
#    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder':'Username'}), max_length=50, label="")
#    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder':'password'}), label="")
