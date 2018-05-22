from django import forms
from django.forms import inlineformset_factory
from django.utils import timezone
from .models import Kunde, VM, Nic, SCSI, Disk
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, MultiField, Submit, Button, HTML
from crispy_forms.bootstrap import TabHolder, Tab, AppendedText, FormActions, Accordion, AccordionGroup


class KundeForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        TabHolder(
            Tab(
                'Basisinformationen',
                Div(Field('name', placeholder="Firmenname"), css_class='col-lg-6'),
                Div(Field('ansprechpartner', placeholder="Name, Vorname"), css_class='col-lg-6'),
                Div(Field('telefon', placeholder="+49 1234/567-890"), css_class='col-lg-6'),
                Div(Field('fax', placeholder="+49 1234/567-891"), css_class='col-lg-6'),
                Div(Field('email', placeholder="abc@def.de"), css_class='col-lg-6'),
                Div(Field('mks', placeholder="MKS-Kundennummer"), css_class='col-lg-6'),
            ),
            Tab(
                'Adresse',
                Div(Field('strasse', placeholder="Musterstraße"), css_class='col-lg-8'),
                Div(Field('hausnummer', placeholder="123"), css_class='col-lg-4'),
                Div(Field('plz', placeholder="98765"), css_class='col-lg-3'),
                Div(Field('ort', placeholder="Musterstadt"), css_class='col-lg-9'),
                Div(FormActions(Submit('save', 'Speichern'), Button('cancel', 'Abbrechen'))),
            )
        )
    )



    class Meta:
        model = Kunde
        fields = ('name', 'strasse', 'hausnummer', 'ort', 'plz', 'ansprechpartner', 'telefon', 'fax', 'email', 'mks',)



class VMForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Div('kunde', css_class='col-lg-3'),
        TabHolder(
            Tab(
                'VM-Basisinformationen',
                Div(Field('name', placeholder="CNP-K-...."), css_class='col-lg-3'),
                Div(Field('creationdate'), css_class='col-lg-3'),
                Div(Field('beschreibung', placeholder="z.B. fuerst-DC01"), css_class='col-lg-6'),
            ),
            Tab(
                'vSphere',
                Div(Field('inventory_location', placeholder="...\CNP-K\CNP-K-"),css_class="col-lg-4"),
                Div(Field('datacenter_cluster'), css_class="col-lg-4"),
                Div(Field('ressource_pool', placeholder="...\CNP-K-"), css_class="col-lg-4"),
                Div('storage', css_class='col-lg-2'),
                Div('vm_version', css_class='col-lg-2'),
                Div('os_version', css_class='col-lg-2'),
                Div('cpu', css_class='col-lg-3'),
                Div(AppendedText('ram', 'GB'), css_class='col-lg-2'),
#                Div(AppendedText('tiera','GB'), css_class='col-lg-2'),
#                Div(AppendedText('tierc','GB'), css_class='col-lg-2'),
            ),
            Tab(
                'Faktura + Reporting',
            ),
            Tab(
                'Archiv',
            ),
        ),
    )


    class Meta:
        model = VM
        fields = ('kunde', 'name', 'creationdate', 'beschreibung', 'inventory_location', 'datacenter_cluster', 'ressource_pool', 'storage', 'vm_version', 'os_version', 'cpu', 'ram',)



class NicForm(forms.ModelForm):
    class Meta:
        model = Nic
        fields = ('network', 'vlanid', 'adapter',)


VMFormSet = inlineformset_factory(VM, Nic, extra=0, min_num=1, fields=('network', 'vlanid', 'adapter'))
