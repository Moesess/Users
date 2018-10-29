from django import forms
from models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('first_name', 'last_name', 'password')

