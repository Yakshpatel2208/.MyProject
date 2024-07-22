from django import forms 
from MyAdmin.models import employee_details,subscription_details,feedback_details,problem_details

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee_details
        fields = ['e_name','e_dob','e_salary','e_daily_work_hours','e_weekend_day','e_contact','e_email','e_password','s_id']

class updateEmp(forms.ModelForm):
    class Meta:
        model = employee_details
        fields = ['e_name','e_salary','e_daily_work_hours','e_weekend_day','e_contact','e_email']
        
class ProblemForm(forms.ModelForm):
    class Meta:
        model = problem_details
        fields = ['p_description','e_id']
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback_details
        fields = ['f_id','f_description','e_id','f_date']

class updatePro(forms.ModelForm):
    class Meta:
        model = problem_details
        fields = ['p_description']