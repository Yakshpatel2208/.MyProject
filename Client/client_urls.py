from django.contrib import admin
from django.urls import path
from Client import client_views

urlpatterns = [
    path('home',client_views.home),
    path('client_index/',client_views.client_index),
    path('register/',client_views.client_singup),
    path('client_sendotp/',client_views.client_sendotp),
    path('client_forgot/',client_views.client_forgot),
    path('client_reset/',client_views.client_set_password),
    path('client_sub/',client_views.client_sub),
    path('client_problem/',client_views.client_problem),
    path('client_login/',client_views.client_login),
    path('client_answer/',client_views.client_answer),
]