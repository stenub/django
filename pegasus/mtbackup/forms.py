from django import forms

from .models import Device

class new_DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('hostname','mgt_ip', 'username', 'password')
