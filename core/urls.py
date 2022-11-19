from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('colaborators/', views.colaborators, name="colaborators"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

