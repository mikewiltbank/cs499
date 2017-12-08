from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='Start'),
    #url(r'^calendar/(?P<id>\d+)/(?P<weekstart>\d+)$', views.calendarView, name='Calendar View'),
    url(r'^gettype/(?P<id>\d+)/$', views.getType, name='Get Type'),
    url(r'^calendar/(?P<id>\d+)/(?P<duration>\d+)/(?P<weekstart>\d{4}-\d{2}-\d{2})/$', views.calendarView, name='Calendar View'),
    #url(r'^changeweek/(?P<id>\d+)/(?P<change>\d+)$', views.weekChange, name='Week Change'),
    url(r'^getinfo/(?P<id>\d+)/$', views.appointmentInfo, name='Appointment Info'),
    ]