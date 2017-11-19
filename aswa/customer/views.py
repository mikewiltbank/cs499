from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'customer/index.html')
def appointmentInfo(request):
    return render(request, 'customer/appointmentInfo.html')
def scheduleView(request):
    return render(request, 'customer/scheduleView.html')