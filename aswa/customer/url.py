from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='Start'),
    url(r'^getinfo/(?P<id>\d+)/$', views.appointmentInfo, name='Appointment Info'),
    url(r'^calendar/', views.scheduleView, name='Calendar View'),
    ]