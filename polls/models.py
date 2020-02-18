from django.db import models
from django.contrib.auth.models import User
from datetime import date
class Department(models.Model):
    dept_name=models.CharField(max_length=50)
    mgr_name=models.CharField(max_length=20)
    def __str__(self):
        return '%s %s' %(self.mgr_name,self.dept_name)
    

class Position(models.Model):
    pos_name=models.CharField(max_length=100)
    def __str__(self):
        return '%s' %(self.pos_name)


class Employee(models.Model):
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob=models.DateField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    date_of_join=models.DateField()
    emp_status=models.BooleanField(default=True)
    mobile_no=models.CharField(max_length=12,blank=True)
    def __int__(self):
        return self.id
   

class Leave(models.Model):
    fst_date = models.DateTimeField()
    til_date = models.DateTimeField()
    count = models.IntegerField(blank=True)
    reason = models.CharField(max_length=50)
    leave_type = models.CharField(max_length=50)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    def days(self):
        return (self.til_date - self.fst_date).days


    def save(self, **kwargs):
        self.count = self.days()
        self.count+=1
        super().save(**kwargs)


class Salary(models.Model):
    acc_no=models.BigIntegerField()
    basic_sal=models.IntegerField()
    pf=models.IntegerField()
    hra=models.IntegerField()
    total_salary=models.IntegerField(null=True, blank=True)
    emp_id=models.ForeignKey(Employee ,on_delete=models.CASCADE, null=False)
    date_of_month=models.DateTimeField()
    count=models.ForeignKey(Leave, on_delete=models.CASCADE)
    def total(self):
        return self.basic_sal + self.pf + self.hra


    def save(self, **kwargs):
        total_s = self.total()
        avg=total_s/30
        c=self.count.count
        total_s=total_s-(avg*c)
        self.total_salary = total_s
        super().save(**kwargs)





































# leader=models.ForeignKey('self',on_delete=models.CASCADE,blank=True)