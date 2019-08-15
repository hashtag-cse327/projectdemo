from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name = 'home'),
    path('aboutus/', views.AboutPage.as_view(), name = 'aboutus'),
] 
