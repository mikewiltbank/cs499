from django.shortcuts import render

# Create your views here.
def customerBase(request):
    return render(request, 'customer/base.html')

def appointmentInfo(request):
    return render(request, 'customer/appointmentInfo.html')

def scheduleView(request):
    return render(request, 'customer/scheduleView.html')