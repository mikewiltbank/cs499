from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^start/$', views.start, name='Business Login'),
    url(r'^login/$', views.login, name='Employee Login'),
    url(r'^tools/$', views.tools, name='Tools'),
    ]