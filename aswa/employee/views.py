#from employee.models import Employees
#from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from employee.forms import NewEmployeeForm


def newEmployee(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the user instance created by the signal
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

@login_required
def tools(request):
    today = datetime.today()
    adjust = (today.weekday() + 1) % 7
    sun = today - timedelta(days=adjust)
    days = [sun]
    for i in range(1,90):
        days.append(sun + (timedelta(days=i)))
    start = None
    if request.user.is_authenticated():
        start = request.user.employees.starttime
        end = request.user.employees.endtime
    temp = datetime.now()
    times = []
    newtime = datetime.combine(temp.date(),start)
    grid = 0
    while newtime.time() != end:
        grid += 1
        b = timedelta(hours=0, minutes=30)
        newtime += b
        times.append(newtime.time())        
    return render(request, 'employee/tools.html', {'days': days, 'times':times, 'grid':grid})