from django import forms
from customer.models import Appointments

#from django.forms.extras.widgets import SelectDateWidget
#YEAR_CHOICES = ('2017','2018','2019')

class NewAppointmentForm(forms.ModelForm):
    name = forms.CharField(max_length=128, required=True, help_text='Full Name')
    phone = forms.CharField(max_length=12, required=True, help_text= '###-###-####')
    email = forms.CharField(max_length=200, required=True, help_text= 'example@email.com')
    #password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False, help_text='For Deleting (Optional)')
    details = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':4}))
    #date = forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES))
    #date = forms.DateField()
    #starttime= forms.TimeField()
    #endtime = forms.TimeField()
    #duration = forms.IntegerField()
    class Meta:
        model = Appointments
        fields = ('name', 'phone', 'email', 'details')
        
class NewTimeForm(forms.ModelForm):
    date = forms.DateField()
    starttime = forms.TimeField()
    endtime = forms.TimeField()
    duration = forms.IntegerField()
    class Meta:
        model = Appointments
        fields = ('date', 'starttime', 'endtime', 'duration')