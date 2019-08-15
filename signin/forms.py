from django import forms
from django.contrib.auth import get_user_model

 
class LoginUsernameForm(forms.Form):
	username = forms.CharField()

class LoginForm(forms.Form):
	#username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


