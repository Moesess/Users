from django import forms
from models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    login = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('login', 'first_name', 'last_name', 'password')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = {'login', 'password'}

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        login = cleaned_data.get("login")
        password = cleaned_data.get("password")

        if login and password:
            if User.objects.filter(login=login, password=password):
                print "zalogowano"
            else:
                raise forms.ValidationError(
                    "problem"
                )


