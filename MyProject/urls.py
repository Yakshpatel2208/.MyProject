"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MyAdmin import views
from Client import client_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('login/',views.login),
    path('form_advanced/',views.form_advanced),
    path('employee_details/',views.employee_table),
    path('update/<int:id>',views.update),
    path('logout/',views.logout),
    path('delete/<int:id>',views.remove),
    path('send_otp/',views.sendotp),
    path('forgot/',views.forgot),
    path('reset/',views.set_password),
    path('insert/',views.insert),
    path('update_problem/<int:id>',views.update_problem),
    path('from_update/',views.formstemp),
    path('problem_details/',views.problem_table),
    path('problem_insert/',views.insert_problem),
    path('delete_problem/<int:id>',views.problem_remove),
    path('feedback_details/',views.feedback_table),
    path('subscriptions_details/',views.subscriptions_table),
    path('profile/',views.profile),
    
    
    path('client/',include('Client.client_urls')),

]
