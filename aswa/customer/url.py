from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='Start'),
    url(r'^calendar/(?P<id>\d+)/$', views.calendarView, name='Calendar View'),
    url(r'^getinfo/(?P<id>\d+)$', views.appointmentInfo, name='Appointment Info'),
    ]