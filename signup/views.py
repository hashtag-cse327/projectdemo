from django.urls import path
from . import views
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import RegisterForm

# Create your views here.

User = get_user_model()

def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form,
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)

	return render(request, "register.html", context)
