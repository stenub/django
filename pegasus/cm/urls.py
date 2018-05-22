from django.conf.urls import url
from django.views.generic import ListView
from cm.models import Kunde, VM, Change
from . import views

urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^kunde/neu/$', views.kunde_neu, name='kunde_neu'),
    url(r'^kunde/liste/$', ListView.as_view(
        model=Kunde, template_name='cm/kunden_liste.html'), name='kunden_liste'),
    url(r'^vm/neu/$', views.vm_neu, name='vm_neu'),
    url(r'^vm/liste/$', ListView.as_view(
        model=VM, template_name='cm/vm_liste.html'), name='vm_liste'),
    url(r'^change/neu/$', views.change_neu, name='change_neu'),
    url(r'^change/liste/$', ListView.as_view(
        model=Change, template_name='cm/change_liste.html'), name='change_liste'),
]
