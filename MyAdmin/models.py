from django.db import models


# Create your models here.

class subscription_details(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=20)
    s_max_problem_solve_qty = models.CharField(max_length=10)
    price = models.IntegerField()
    class Meta:
        db_table="subscription_details"
        
class employee_details(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=20)
    e_dob = models.DateField()
    e_salary = models.IntegerField()
    e_daily_work_hours = models.IntegerField()
    e_weekend_day = models.IntegerField()
    e_contact = models.CharField(max_length=10)
    e_email = models.CharField(max_length=50)
    e_password = models.CharField(max_length=15)
    s_id = models.ForeignKey(subscription_details, on_delete = models.CASCADE)
    otp=models.CharField(max_length=10,null=True)
    otp_used=models.IntegerField()
    
    class Meta:
        db_table="employee_details"

class problem_details(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_description = models.CharField(max_length=100)
    e_id = models.ForeignKey(employee_details, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "problem_details"
        
class improvement_details(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_theme = models.CharField(max_length=100)
    i_objective_key_results = models.CharField(max_length=200)
    p_id = models.ForeignKey(problem_details,on_delete=models.CASCADE)
    generated_date = models.DateField()

    class Meta:
        db_table = "improvement_details"

class feedback_details(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_description = models.CharField(max_length=100)
    e_id = models.ForeignKey(employee_details,on_delete=models.CASCADE)
    f_date = models.DateField()
    
    class Meta:
        db_table = "feedback_details"
