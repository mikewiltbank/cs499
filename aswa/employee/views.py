from django.shortcuts import render
from employee.models import Business
from django.http.response import HttpResponseRedirect

# Create your views here.
def start(request):
    if request.method == "POST" :
        def register(request):
            businessName = request.POST['businessName']
            business_pwd = request.POST['business_pwd']
            business_obj = Business(name = businessName, password = business_pwd)
            business_obj.save()
            
            return HttpResponseRedirect('employee/employeelogin.html')
    return render(request, 'employee/businesslogin.html')

def login(request):
    return render(request, 'employee/employeelogin.html')

def tools(request):
    return render(request, 'employee/tools.html')

