#from employee.models import Employees
#from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from employee.forms import NewEmployeeForm

@login_required
def tools(request):
    return render(request, 'employee/tools.html')

def newEmployee(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.employees.full_name = form.cleaned_data.get('full_name')
            user.employees.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('Tools')
    else:
        form = NewEmployeeForm()
    return render(request, 'employee/newemployee.html', {'form': form})