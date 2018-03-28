from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_device', views.new_device),
    path('show_device', views.show_device),
    path('get_backup', views.get_backup),
    
]
