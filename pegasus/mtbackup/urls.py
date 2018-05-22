from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('device_list', views.device_list, name='device_list'),
    path('device_new', views.device_new, name='device_new'),
    #path('device_list/<slug:slug>/delete', views.device_delete, name='device_delete'),
    path('schedule_list', views.schedule_list, name='schedule_list'),
    path('schedule_new', views.schedule_new, name='schedule_new'),
    path('', views.base, name='base'),
]