from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()



class LoginUsernameForm(forms.Form):
	username = forms.CharField()

class LoginForm(forms.Form):
	#username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(
			widget=forms.EmailInput(
				attrs={
					"class": "form-control",
					"placeholder": "Your email"
				}
				)
			)
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username exists")
			return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email exists")
			return email


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("password must match.")
		return data