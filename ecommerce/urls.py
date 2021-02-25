from django.contrib import admin
from django.urls import path
from ecommerce import views
urlpatterns = [
    path("",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("login",views.login,name='login'),
    path("register",views.register,name='register')
]