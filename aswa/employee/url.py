from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#from django.conf.urls import url, include

urlpatterns = [
    url(r'^tools/$', views.tools, name='Tools'),
    url(r'^new/$', views.newEmployee, name='New Employee'),
    url(r'^login/$', auth_views.login, {'template_name': 'employee/employeelogin.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    ]