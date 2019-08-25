from django.urls import path
from . import views
from django.views.generic import TemplateView


# Create your views here.

class HomePage(TemplateView):
	template_name = 'index.html'

class AboutPage(TemplateView):
	template_name = 'aboutus.html'

class ShomePage(TemplateView):
	template_name = 'sindex.html'

