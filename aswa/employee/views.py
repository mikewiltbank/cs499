from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from customer.models import Appointments
from employee.models import AppointmentTypes, Employees
from employee.forms import NewEmployeeForm, CustomUnavailableForm, DaysForm

def newEmployee(request):
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            today = datetime.today()
            user = form.save()
            user.refresh_from_db()  # load the user instance created by the signal
            user.employees.full_name = form.cleaned_data.get('full_name')
            user.employees.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('Tools', weekstart=today)
    else:
        form = NewEmployeeForm()
    return render(request, 'employee/newemployee.html', {'form': form})

@login_required
def welcome(request):
    today = datetime.today().strftime('%Y-%m-%d')
    return redirect('Tools', weekstart=today)

@login_required
def tools(request, weekstart):
    cuForm = CustomUnavailableForm()
    daysForm = DaysForm()
    today = datetime.strptime(weekstart , '%Y-%m-%d')
    adjust = (today.weekday() + 1) % 7
    saturday = (today - timedelta(days=adjust)) - timedelta(days=1)
    days = [saturday]
    for i in range(1,9):
        days.append(saturday + (timedelta(days=i)))
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
    eid = request.user.employees.id
    appointments = Appointments.objects.filter(employee_id=eid)
    types = AppointmentTypes.objects.filter(employee_id=eid)
    sun = []
    mon = []
    tue = []
    wed = []
    thur = []
    fri = []
    sat = []
    for appointment in appointments:
        if appointment.date.strftime('%Y-%m-%d') == days[1].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            sun.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[2].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            mon.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[3].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            tue.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[4].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            wed.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[5].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            thur.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[6].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            fri.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[7].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            sat.append(appointment)
    if request.method == 'POST':
        if request.POST['form-type'] == "appointmentDelete": # test the form type
            aEmail = request.POST['email']
            aDate = request.POST['date']
            Appointments.objects.get(date=aDate, email=aEmail).delete()
            return redirect('Tools', weekstart=aDate )
        elif request.POST['form-type'] == "startEndTime":
            startDay = request.POST['startDay']
            endDay = request.POST['endDay']
            thisEmployee = Employees.objects.get(id=eid)
            thisEmployee.starttime = startDay
            thisEmployee.endtime = endDay
            thisEmployee.save()
            #typesForm = StartEndForm(request.POST)
            #if typesForm.is_valid():
                #appointmentTypes = form.save(commit=False)
                #aDate = form.cleaned_data['date'].strftime('%Y-%m-%d')
                #aEndTime = form.cleaned_data['endtime'].strftime('%H:%M')
            return redirect('Welcome')
        elif request.POST['form-type'] == "appointmentTypes":
            aName = request.POST['typeName']
            aDuration = request.POST['optradio']
            update = AppointmentTypes(name=aName, duration=aDuration, employee_id=eid)
            update.save()
            #typesForm = AppointmentTypesForm(request.POST)
            #if typesForm.is_valid():
            return redirect('Welcome')
        elif request.POST['form-type'] == "updateDays":
            day1 = request.POST.get['sun']
            day2 = request.POST.get['mon']
            day3 = request.POST['tue']
            day4 = request.POST['wed']
            day5 = request.POST['thur']
            day6 = request.POST['fri']
            day7 = request.POST['sat']
            thisEmployee = Employees.objects.get(id=eid)
            thisEmployee.sun = day1
            thisEmployee.mon = day2
            thisEmployee.sun = day3
            thisEmployee.mon = day4
            thisEmployee.sun = day5
            thisEmployee.mon = day6
            thisEmployee.sun = day7
            thisEmployee.save()
            return redirect('login')
        elif request.POST['form-type'] == "customUnavailable":
            who = Employees.objects.get(id=eid)
            #uDate = request.POST.filter['date']
            sTime = request.POST['starttime']
            eTime = request.POST['endtime']
            temp2 = datetime.now()
            a = datetime.combine(temp2.date(),datetime.strptime(eTime, '%H:%M').time()) - datetime.combine(temp2.date(),datetime.strptime(sTime, '%H:%M').time())
            durat = (a / timedelta(hours=0, minutes=30)) * 40
            #datetime.strptime(sTime, '%H:%M')
            update2 = Appointments(name = "Custom Unavailable", phone = "9999999999", email = "empty@email.com", details = "empty", date = "2017-12-10", starttime = sTime, endtime = eTime, employee = who, duration = durat)
            update2.save()
            #return redirect('Welcome')            
            '''
            #if cuForm.is_valid():
            customAppointment = cuForm.save(commit=False)
            #uDate = form.cleaned_data['date']
            customAppointment.employee = who
            customAppointment.name = "Custom Unavailable"
            customAppointment.phone = "9999999999"
            customAppointment.email = "empty@email.com"
            customAppointment.details = "empty"
            customAppointment.date = "2017-12-12" #form.cleaned_data['date'].strftime('%Y-%m-%d')
            customAppointment.starttime = "8:00"#form.cleaned_data['starttime'].strftime('%H:%M')
            customAppointment.endtime = "9:00"#form.cleaned_data['endtime'].strftime('%H:%M')
            customAppointment.duration = "120"
            customAppointment.save()
            '''
            return redirect('Welcome')
                #return redirect('Tools', weekstart=uDate)  
    return render(request, 'employee/tools.html', {'form':cuForm, 'daysForm':daysForm, 'types':types, 'days': days, 'times':times, 'grid':grid,
                                                   'sun':sun, 'mon':mon, 'tue':tue,'wed':wed, 'thur':thur, 
                                                   'fri':fri, 'sat':sat })
    
def dropType(request, typeid):
    AppointmentTypes.objects.get(id=typeid).delete()
    return redirect('Welcome')
    