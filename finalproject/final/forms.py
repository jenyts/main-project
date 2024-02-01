from django import forms
from . models import HomeWork,HomeWorkQtn,Poll,Choice,StudyMaterials
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Regform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Your Username'
        }
    ))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Enter Your Email id'
        }
    ))
    password1=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Your Password'
        }
    ))
    password2=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter Your Password Again For Confirmation'
        }
    ))
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter your Firstname'
        }
    ))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter your Lastname'
        }
    ))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]



class Hw(forms.ModelForm):
    
    class Meta:
        model=HomeWork
        fields='__all__'

class HwQtn(forms.ModelForm):
    class Meta:
        model=HomeWorkQtn
        fields='__all__'

class PollForm(forms.ModelForm):
    class Meta:
        model=Poll
        fields='__all__'

class ChoiceForm(forms.ModelForm):
    class Meta:
        model=Choice
        fields='__all__'        

class MaterialForm(forms.ModelForm):
    class Meta:
        model=StudyMaterials
        fields='__all__'

