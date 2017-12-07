from django.shortcuts import render, redirect
from customer.forms import NewAppointmentForm
from employee.models import Employees, AppointmentTypes
from customer.models import Appointments
from datetime import datetime, timedelta, time
#from django.forms import ModelForm

# Create your views here.
def customerBase(request):
    return render(request, 'customer/base.html')

def start(request):
    employees = Employees.objects.values('id', 'full_name')
    #employee_id = Employees.objects.get(id='4').id
    #request.session['employee_id'] = employee_id
    #temp = employee_id
    return render(request, 'customer/customerstart.html', {'employees': employees})

def appointmentInfo(request, id, value):
    '''
    today = datetime.today()
    adjust = (today.weekday() + 1) % 7
    sun = today - timedelta(days=adjust)
    days = [sun]
    for i in range(1,90):
        days.append(sun + (timedelta(days=i)))
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
    appointments = list(Appointments.objects.filter(employee_id=id))
    sun = []
    mon = []
    tue = []
    wed = []
    thur = []
    fri = []
    sat = []
    for appointment in appointments:
        if appointment.date.strftime('%Y-%m-%d') == days[0].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                sun.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                sun.append((appointment.starttime.hour - start.hour)*80)
        if appointment.date.strftime('%Y-%m-%d') == days[1].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                mon.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                mon.append((appointment.starttime.hour - start.hour)*80)
        if appointment.date.strftime('%Y-%m-%d') == days[2].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                tue.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                tue.append((appointment.starttime.hour - start.hour)*80)
        if appointment.date.strftime('%Y-%m-%d') == days[3].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                wed.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                wed.append((appointment.starttime.hour - start.hour)*80)
        if appointment.date.strftime('%Y-%m-%d') == days[4].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                thur.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                thur.append((appointment.starttime.hour - start.hour)*80)
        if appointment.date.strftime('%Y-%m-%d') == days[5].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                fri.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                fri.append((appointment.starttime.hour - start.hour)*80)
        if appointment.date.strftime('%Y-%m-%d') == days[6].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                sat.append(((appointment.starttime.hour - start.hour)*80)+40)
            else:
                sat.append((appointment.starttime.hour - start.hour)*80)  '''      
    if request.method == 'POST':
        #employee_id = request.session['employee_id']
        who = Employees.objects.get(id=id)
        aDate = '2017-12-09'
        #aDate = datetime.date(day=5, year=2017, month=12)
        #aStarttime = datetime.time(hour=8, minute=0)
        aStarttime = '10:00'
        #aEndtime = datetime.time(hour=9, minute=0)
        aEndtime = '11:00'
        aDuration = 80        
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            appointments = form.save(commit=False)
            appointments.employee = who
            appointments.date = aDate
            appointments.starttime = aStarttime
            appointments.endtime = aEndtime
            appointments.duration = aDuration
            appointments.save()
            #appointments_instance = Appointments.objects.create()
            return redirect('Start')
    
        return render(request, 'customer/appointmentInfo.html')
    else:
        form = NewAppointmentForm()
    return render(request, 'customer/appointmentInfo.html', {'form': form})

class Day(object):
    aBegin = ""
    duration = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, aBegin, duration):
        self.aBegin = aBegin
        self.duration = duration

def make_student(aBeing, duration):
    day = Day(aBeing, duration)
    return day

def calendarView(request, id):
    today = datetime.today()
    adjust = (today.weekday() + 1) % 7
    sunday = today - timedelta(days=adjust)
    days = [sunday]
    for i in range(1,90):
        days.append(sunday + (timedelta(days=i)))
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
        if appointment.date.strftime('%Y-%m-%d') == days[0].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            sun.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[1].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            mon.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[2].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            tue.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[3].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            wed.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[4].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            thur.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[5].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            fri.append(appointment)
        if appointment.date.strftime('%Y-%m-%d') == days[6].strftime('%Y-%m-%d') :
            if appointment.starttime.minute == 30:
                aBegin = ((appointment.starttime.hour - start.hour)*80)+40
            else:
                aBegin = (appointment.starttime.hour - start.hour)*80
            setattr(appointment, 'aBegin', aBegin)
            sat.append(appointment)
                  
    return render(request, 'customer/scheduleView.html', {'id':id, 'types': types, 'days': days, 'times':times, 
                                                          'grid':grid, 'sun':sun, 'mon':mon, 'tue':tue,
                                                          'wed':wed, 'thur':thur, 'fri':fri, 'sat':sat})