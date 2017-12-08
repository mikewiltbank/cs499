from django.shortcuts import render, redirect
from customer.forms import NewAppointmentForm, NewTimeForm
from employee.models import Employees, AppointmentTypes
from customer.models import Appointments
from datetime import datetime, timedelta

# Create your views here.
def customerBase(request):
    return render(request, 'customer/base.html')

def start(request):
    employees = Employees.objects.values('id', 'full_name')
    return render(request, 'customer/customerstart.html', {'employees': employees})

def getType(request, id):
    today = datetime.today()
    types = AppointmentTypes.objects.filter(employee_id=id)
    return render(request, 'customer/gettype.html', {'id':id, 'today':today, 'types':types })

def calendarView(request, id, duration, weekstart):
    today = datetime.strptime(weekstart , '%Y-%m-%d')
    adjust = (today.weekday() + 1) % 7
    saturday = (today - timedelta(days=adjust)) - timedelta(days=1)
    days = [saturday]
    for i in range(1,9):
        days.append(saturday + (timedelta(days=i)))
    start = Employees.objects.get(id=id).starttime
    end = Employees.objects.get(id=id).endtime
    temp = datetime.now()
    times = []
    newtime = datetime.combine(temp.date(),start)
    grid = 0
    while newtime.time() != end:
        grid += 1
        b = timedelta(hours=0, minutes=30)
        newtime += b
        times.append(newtime.time())
    types = AppointmentTypes.objects.filter(employee_id=id)
    appointments = Appointments.objects.filter(employee_id=id)
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
        form = NewTimeForm(request.POST)
        if form.is_valid():
            appointments = form.save(commit=False)            
            request.session['date'] = form.cleaned_data['date'].strftime('%Y-%m-%d')
            request.session['startTime'] = form.cleaned_data['starttime'].strftime('%H:%M')
            request.session['endTime'] = form.cleaned_data['endtime'].strftime('%H:%M')
            request.session['duration'] = form.cleaned_data['duration']
            return redirect('Appointment Info', id=id)
        else:
            form = NewTimeForm()
    return render(request, 'customer/scheduleView.html', {'id':id, 'types': types, 'dur':duration, 'days': days, 'times':times, 
                                                          'grid':grid, 'sun':sun, 'mon':mon, 'tue':tue,
                                                          'wed':wed, 'thur':thur, 'fri':fri, 'sat':sat})

def appointmentInfo(request, id):     
    if request.method == 'POST':
        who = Employees.objects.get(id=id)
        aDate = request.session['date']
        aStarttime = request.session['startTime']
        aEndtime = request.session['endTime'] 
        aDuration = request.session['duration']       
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            appointments = form.save(commit=False)
            appointments.employee = who
            appointments.date = aDate
            appointments.starttime = aStarttime
            appointments.endtime = aEndtime
            appointments.duration = aDuration
            appointments.save()
            return redirect('Start')
    
        return render(request, 'customer/appointmentInfo.html')
    else:
        form = NewAppointmentForm()
    return render(request, 'customer/appointmentInfo.html', {'form': form})