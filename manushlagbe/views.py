from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm, LoginUsernameForm

def home_page(request):
	context = {
		"title":"Manush Lagbe",
		
	}
	if request.user.is_authenticated :
		context["premium_content"] = "YES"
	return render(request, "home_page.html", context)

def signup(request):
	if request.method == "POST":
		print(request.POST)
	return render(request, "signup/view.html", {})

def login_page(request):
	username = LoginUsernameForm(request.POST or None)
	form = LoginForm(request.POST or None)
	context = {
		"username": username,
		"form": form,
	}
	print("User logged in")
	#print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
	if username.is_valid():
		print(username.cleaned_data)
		Username = username.cleaned_data.get("username")
		Password = form.cleaned_data.get("password")
		user = authenticate(request, username=Username, password=Password)
		print(user)
		#print(request.user.is_authenticated())
		if user is not None:
			#print(request.user.is_authenticated())
			login(request, user)
			#Redirect to a success page.
			#context['form'] = LoginForm()
			return redirect("/")
		else:
			#Return an 'invalid login' error message.
			print ("Errror")
	return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request, "auth/register.html", context)
