from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from products import views
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
