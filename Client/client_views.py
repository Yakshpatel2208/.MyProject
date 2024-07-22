from django.shortcuts import render, redirect
from MyAdmin.models import employee_details,subscription_details,problem_details,feedback_details
from django.contrib import messages
from django.http import HttpResponse
from MyAdmin.forms import EmployeeForm,updateEmp,ProblemForm,FeedbackForm,updatePro
import sys
from django.core.mail import send_mail
from MyProject import settings
import random
from Client.utils import generate_content

# Create your views here.

def home(request):
    return render(request, 'home.html')

def client_index(request):
    return render(request, 'client_index.html')

def client_singup(request):
    print("--------- sign up--------------")
    c = subscription_details.objects.all()
    
    print(request.method)
    
    if  request.method == "POST":
        print("----------------------- if")
        fr = EmployeeForm(request.POST)
        print(fr)
        if fr.is_valid():
            try:
                print("----------------------- try")
                fr.save()
                return redirect("/client/client_index/")
            except:
                
                print("----------",sys.exc_info())
    else:
        print("-----------------------")
        return render(request,"client_signup.html",{'sub':c})
    
def client_login(request):
    print("--------------------------------------------------------------")
    if request.method == "POST":
        e = request.POST["e_email"]
        p = request.POST["e_password"]
        
        print("--------------------------------")
        
        u = employee_details.objects.filter(e_email=e,e_password=p).count()
        
        if u == 1:
            
            print("------------------yaksh-----------------------")
            obj = employee_details.objects.get(e_email=e)
            request.session['e_name'] = obj.e_name
            request.session['e_email'] = obj.e_email
            request.session['e_eid'] = obj.e_id
            
            if request.POST.get("remember"):
                response = redirect("/client/client_index/")
                response.set_cookie('cookie_clientemail',e,3600*24*365*2)
                response.set_cookie('cookie_clientpassword',p,3600*24*365*2)
                return response
            
            return redirect('/client/client_index/')
        else:
            print("------------------ELSE")
            messages.error(request,"Invalid email or password")
            return redirect("/client/client_index/")
    else:
        return render(request,"client_login.html")

def client_forgot(request):
    return render(request,"client_forgot.html")

def client_sendotp(request):
    otp1 = random.randint(1000,9999)
    e = request.POST['e_email']
    request.session["temail"] = e
    obj = employee_details.objects.filter(e_email=e).count()
    if obj == 1:
        
        val = employee_details.objects.filter(e_email=e).update(otp=otp1 ,otp_used=0)
        
        subject = 'OTP varifiction'
        message = str(otp1)
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [e,]
        
        send_mail(subject, message, email_form, recipient_list)
        return render(request, 'client_reset.html')
    
def client_set_password(request):
    if request.method ==  "POST":
        t_otp = request.POST["otp"]
        t_pass = request.POST["password"]
        t_cpass = request.POST["cpassword"]
        
        if t_pass == t_cpass:
            
            e = request.session['temail']
            val = employee_details.objects.filter(e_email = e, otp = t_otp,otp_used = 0).count()
            
            if val == 1:
                employee_details.objects.filter(e_email = e).update(otp_used = 1, e_password = t_pass)
                return redirect("/client/client_index")   
            else:
                messages.error(request,"Invalid OTP")
                return render(request, "client_forgot.html")
        else:
            messages.error(request,"New password and Confirm password does not match")
            return render(request, "client_reset.html") 
    else:
        return redirect("client/client_forgot/")
    
def client_sub(request):
    c = subscription_details.objects.all()
    return render(request, 'client_subscribtions.html',{'sub':c})

def client_problem(request):
    if request.method == "POST":
        fr = ProblemForm(request.POST)
        if fr.is_valid():
            try:
                fr.save()
                # problem=request.POST["p_description"]
                # ans=generate_content(problem)
                return redirect("/client/client_answer/")
            except:
                print("----------",sys.exc_info())
    else:
        return render(request,"client_problem.html")
    
def client_answer(request):


    prob=problem_details.objects.filter(e_id=request.session['e_eid'])

    return render(request,'client_answer.html',{'pro':prob})