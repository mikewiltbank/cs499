from django import forms

class newBusiness(forms.Form):
    businessName = forms.CharField(label="Enter Unique Business Name", max_length=128)
    business_pwd = forms.CharField(label="Password", max_length=128)