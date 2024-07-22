from django.shortcuts import render, redirect
from MyAdmin.models import employee_details,subscription_details,problem_details,feedback_details
from django.contrib import messages
from django.http import HttpResponse
import sys
import random
from MyProject import settings
from django.core.mail import send_mail
from MyAdmin.forms import EmployeeForm,updateEmp,ProblemForm,FeedbackForm,updatePro

# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_advanced(request):
    return render(request, 'form-advanced.html')

def employee_table(request):
    emp_det = employee_details.objects.all()   
    return render(request, 'employee-table.html',{'emp':emp_det})


def subscriptions_table(request):
    sub_det = subscription_details.objects.all() 
      
    return render(request, 'subscriptions-table.html',{'sub':sub_det})

def feedback_table(request):
    feed_det = feedback_details.objects.all() 
    emp_det = employee_details.objects.all()  
    return render(request, 'feedback-table.html',{'feed':feed_det,'emp':emp_det})

def problem_table(request):
    pro_det = problem_details.objects.all()
    
    emp_det = employee_details.objects.all()
    return render(request, 'problem-table.html',{'pro':pro_det,'emp':emp_det})
    
def remove(request,id):
    emp_det=employee_details.objects.filter(e_id=id)
    emp_det.delete()
    return redirect("/employee_details/")

def login(request):
    if request.method == "POST":
        e = request.POST["email"]
        p = request.POST["password"]
        
        print("--------------------------------")
        
        u = employee_details.objects.filter(e_email=e,e_password=p).count()
        
        if u == 1:
            obj = employee_details.objects.get(e_email=e)
            request.session['ename'] = obj.e_name
            request.session['email'] = obj.e_email
            request.session['eid'] = obj.e_id
            
            if request.POST.get("remember"):
                response = redirect("/index/")
                response.set_cookie('cookie_email',e,3600*24*365*2)
                response.set_cookie('cookie_password',p,3600*24*365*2)
                return response
            
            return redirect('/index/')
        else:
            print("------------------ELSE")
            messages.error(request,"Invalid email or password")
            return redirect("/login/")
    else:
        return render(request,"auth-login.html")
       
def logout(request):   
    return redirect('/login/')

def sendotp(request):
    otp1 = random.randint(1000,9999)
    e = request.POST['email']
    request.session["temail"] = e
    obj = employee_details.objects.filter(e_email=e).count()
    if obj == 1:
        
        val = employee_details.objects.filter(e_email=e).update(otp=otp1 ,otp_used=0)
        
        subject = 'OTP varifiction'
        message = str(otp1)
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [e,]
        
        send_mail(subject, message, email_form, recipient_list)
        return render(request, 'auth-forgot-password.html')

def set_password(request):
    if request.method ==  "POST":
        t_otp = request.POST["otp"]
        t_pass = request.POST["password"]
        t_cpass = request.POST["cpassword"]
        
        if t_pass == t_cpass:
            
            e = request.session['temail']
            val = employee_details.objects.filter(e_email = e, otp = t_otp,otp_used = 0).count()
            
            if val == 1:
                employee_details.objects.filter(e_email = e).update(otp_used = 1, e_password = t_pass)
                return redirect("/login")   
            else:
                messages.error(request,"Invalid OTP")
                return render(request, "forgot.html")
        else:
            messages.error(request,"New password and Confirm password does not match")
            return render(request, "auth-forgot-password.html") 
    else:
        return redirect("/forgot/")
    
def forgot(request):
    return render(request,"forgot.html")

def update(request,id):
    e = employee_details.objects.get(e_id=id)
    c = subscription_details.objects.all()
    if request.method == "POST":
        fr= updateEmp(request.POST,instance=e)
        print("--------------------if")
        if fr.is_valid() :   
            try:
                print("----------------------- try")
                fr.save()
                request.session['ename'] = e.e_name
                request.session['email'] = e.e_email
                return redirect("/employee_details/")
            except:
                print("----------",sys.exc_info())
    else:
        return render(request,"employee_update.html",{'emp':e,'sub':c})

def insert(request):
    print("-----------------------")
    c = subscription_details.objects.all()
    
    if request.method == "POST":
        print("----------------------- if")
        fr = EmployeeForm(request.POST)
        print(fr)
        if fr.is_valid():
            try:
                print("----------------------- try")
                fr.save()
                return redirect("/employee_details/")
            except:
                
                print("----------",sys.exc_info())
    else:
        print("-----------------------")
        return render(request,"employee_Insert.html",{'sub':c})

def update_problem(request,id):
    e = problem_details.objects.get(p_id=id)
  
 
    if request.method == "POST":
        fr= updatePro(request.POST,instance=e)
        print("--------------------if")
        if fr.is_valid() :   
            try:
                print("----------------------- try")
                fr.save()
                return redirect("/problem_details/")
            except:
                print("----------",sys.exc_info())
    else:
        return render(request,"problem_update.html",{'emp':e})

def formstemp(request):
    return render(request,"form-elements.html")

def insert_problem(request):
    print("-----------------------")
    c = problem_details.objects.all()
    e = employee_details.objects.all()
    if request.method == "POST":
        print("----------------------- if")
        fr = ProblemForm(request.POST)
        print(fr)
        if fr.is_valid():
            try:
                print("----------------------- try")
                fr.save()
                return redirect("/problem_details/")
            except:
                
                print("----------",sys.exc_info())
    else:
        print("-----------------------")
        return render(request,"problem_insert.html",{'emp':e})
    
def problem_remove(request,id):
    pro_det = problem_details.objects.filter(p_id=id)
    pro_det.delete()
    return redirect("/problem_details/")
    

def profile(request):
    return render(request, 'page-profile.html')
