from django import forms
from .models import userdata

class userForm(forms.ModelForm):
    class Meta:
        model=userdata
        fields='__all__'