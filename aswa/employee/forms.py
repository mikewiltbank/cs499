from django import forms
#from employee.models import Employee

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import RadioSelect

class NewEmployeeForm(UserCreationForm):
    full_name = forms.CharField(max_length=200, required=True, help_text='Full Name')
    email = forms.CharField(max_length=200, required=True, help_text='Enter Email')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2', )
        

RADIO_DURATIONS = [['1','30 min'],['2','1 hr'],['3','1 hr 30 min'], ['4','2 hr']]

class AppointmentTypesForm(forms.Form):
    name = forms.CharField(max_length=128, required=True, help_text='Full Name')
    duration = forms.ChoiceField( widget=RadioSelect(), choices=RADIO_DURATIONS)
    class Meta:
        fields = ('name', 'duration')
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