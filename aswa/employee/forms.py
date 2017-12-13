from django import forms
#from employee.models import Employee

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import RadioSelect
from customer.models import Appointments
from employee.models import Employees

YEAR_CHOICES = ('2017','2018','2019')

class NewEmployeeForm(UserCreationForm):
    full_name = forms.CharField(max_length=200, required=True, help_text='Full Name')
    email = forms.CharField(max_length=200, required=True, help_text='Enter Email')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2', )
        

class CustomUnavailableForm(forms.Form):
    #name = forms.CharField(max_length=128, required=True, help_text='Full Name')
    #phone = forms.CharField(max_length=12, required=True, help_text= '###-###-####')
    #email = forms.CharField(max_length=200, required=True, help_text= 'example@email.com')
    #password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False, help_text='For Deleting (Optional)')
    #details = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':4}))
    date = forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES))
    #date = forms.DateField()
    starttime= forms.TimeField(help_text='8:00')
    endtime = forms.TimeField(help_text='17:00')
    #duration = forms.IntegerField()
    class Meta:
        #model = Appointments
        fields = ('date', 'starttime', 'endtime')

class DaysForm(forms.ModelForm):
    sun = forms.BooleanField(initial=True)
    mon = forms.BooleanField(initial=True)
    tue = forms.BooleanField(initial=True)
    wed = forms.BooleanField(initial=True)
    thur = forms.BooleanField(initial=True)
    fri = forms.BooleanField(initial=True)
    sat = forms.BooleanField(initial=True)

    class Meta:
        model = Employees
        fields = ('sun', 'mon' ,'tue', 'wed', 'thur', 'fri', 'sat')

class AppointmentDeleteForm(forms.ModelForm):
    date = forms.DateField()
    email = forms.TimeField()
    class Meta:
        model = Appointments
        fields = ('date', 'email')        

#RADIO_DURATIONS = [['1','40'],['2','1 hr'],['3','1 hr 30 min'], ['4','2 hr']]
RADIO_DURATIONS = (
    ('1', '40'),
    ('2', '80'),
    ('3', '120'),
    ('4', '160'),
    ('5', '200'),
    ('6', '240'),
)

class AppointmentTypesForm(forms.Form):
    name = forms.CharField(max_length=128, required=True, help_text='Full Name')
    duration = forms.ChoiceField( widget=RadioSelect(), choices=RADIO_DURATIONS)
    class Meta:
        fields = ('name', 'duration')

class StartEndForm(forms.Form):
    starttime = forms.TimeField()
    endtime = forms.TimeField()
    class Meta:
        model = Appointments
        fields = ('starttime', 'endtime')
    
'''
class newBusiness(forms.Form):
    businessName = forms.CharField(label="Enter Unique Business Name", max_length=128)
    business_pwd = forms.CharField(label="Password", max_length=128)

class LoginForm(forms.Form):
    employeeName = forms.CharField(max_length = 128)
    employee_pwd = forms.CharField(widget = forms.PasswordInput())
    
    def clean_message(self):
        employeeName = self.cleaned_data.get("employeeName")
        dbuser = Employee.objects.filter(name = employeeName)
        
        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return employeeName
'''