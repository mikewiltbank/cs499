from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getinfo/', views.appointmentInfo, name='Appointment Info'),
    url(r'^calendar/', views.scheduleView, name='Calendar View'),
    ]