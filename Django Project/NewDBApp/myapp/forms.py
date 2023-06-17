from django import forms
from .models import userinfo

class userForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=['name','email','sub','dob']
