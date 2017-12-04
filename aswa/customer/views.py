from django.shortcuts import render, redirect
from customer.forms import NewAppointmentForm
from employee.models import Employees
from customer.models import Appointments
from datetime import datetime, timedelta
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

def appointmentInfo(request, id):
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
                sat.append((appointment.starttime.hour - start.hour)*80)        
    if request.method == 'POST':
        #employee_id = request.session['employee_id']
        who = Employees.objects.get(id=id)
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            appointments = form.save(commit=False)
            appointments.employee = who
            appointments.save()
            #appointments_instance = Appointments.objects.create()
            return redirect('Start')
    
        return render(request, 'customer/appointmentInfo.html')
    else:
        form = NewAppointmentForm()
    return render(request, 'customer/appointmentInfo.html', 
                  {'form': form, 'days': days, 'times':times, 'grid':grid, 'sun':sun, 'mon':mon, 
                   'tue':tue,'wed':wed, 'thur':thur, 'fri':fri, 'sat':sat})


def scheduleView(request):
    return render(request, 'customer/scheduleView.html')