from django import forms
from Taekwondo.models import Players
from Taekwondo.models import Results
from django.forms import ModelForm
from django.contrib.auth.models import User

class PlayerForm(ModelForm):
    class Meta:
        model = Players
        fields = ['name','gender','age','agegroup','weight','weightcategory','PlayingFor','state','country']
        db_table = 'Players'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','email','password']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ['agegroup','gender','weightcategory','gold','silver','bronze1','bronze2']
        db_table = 'Results'
