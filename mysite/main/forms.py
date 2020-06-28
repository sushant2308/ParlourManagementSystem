from django import forms
from django.contrib.auth.models import User
from .models import Appointment,Services
from django.contrib.auth.forms import UserCreationForm
from functools import partial
DateInput = partial(forms.DateInput, {'id': 'datepicker'})

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
class DateInput(forms.DateInput):
    input_type='date'


class CreateAppointment(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ("service","date", "time")
        widgets = {'date':DateInput()}

    def __init__(self, *args, **kwargs):
        super(CreateAppointment,self).__init__(*args, **kwargs)
        
        self.fields['date'].widget=DateInput()
        self.fields['date'].widget.attrs={'class':'form-control'}
        self.fields['service'].widget.attrs={'class':'form-control','data-style':'btn-primary','style':"color : #28a950 !important;"}
        self.fields['time'].widget.attrs={'class':'form-control'}

class Addservice(forms.ModelForm):
    class Meta:
        model=Services
        fields = ('name','price','image')
    
    def __init__(self, *args, **kwargs):
        super(Addservice,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'