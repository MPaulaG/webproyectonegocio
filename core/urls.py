from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('colaborators/', views.colaborators, name="colaborators"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
   
   
]