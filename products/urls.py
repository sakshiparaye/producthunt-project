from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from products import views
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]
