from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.customerBase, name='Customer Base'),
    url(r'^getinfo/', views.appointmentInfo, name='Appointment Info'),
    url(r'^calendar/', views.scheduleView, name='Calendar View'),
    ]