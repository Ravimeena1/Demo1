from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm,LeaveForm,DepartmentForm,SalaryForm,PositionForm
from .filter import *
from  polls.models import  Employee,Leave,Department,Salary,Position
from django.contrib.auth.models import User

def index(request):
    return render(request,'example.html')


def user_profile(request):
    user=get_object_or_404(User,pk=request.user.id)
    return render(request,"profile.html",{'user':user})


def add_employee(request):
    if request.method == 'POST':
        form1=EmployeeForm(request.POST)
        if form1.is_valid():
                
            return HttpResponseRedirect(reverse('poll'))
    form1= EmployeeForm()
    return render(request, 'add_employee.html', {'form1': form1})


def update_emp(request,pk):
    employee=Employee.objects.get(id=pk)
    user=User.objects.get(employee.user_id)
    form1=EmployeeForm(instance= employee)
    if request.method=='POST':
        if form1.is_valid():
            form1=EmployeeForm(request.POST,instance= employee)
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1= EmployeeForm(instance= employee)
    return render(request, 'update_emp.html', {'form1': form1}  )  


def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employee_list.html', {'employee':employee})  


def delete_emp(request,pk):
    emp=Employee.objects.get(id=pk)
    if request.method=='POST':
        emp.delete()
        return HttpResponseRedirect(reverse('poll'))
    form1=EmployeeForm(instance=emp)
    return render(request, 'delete_emp.html', {'form1': form1}  )  


def add_leave(request):
    if request.method == 'POST':
        form1=LeaveForm(request.POST)
        if form1.is_valid():
            if request.POST.get('fst_date')<=request.POST.get('til_date'):
                form1.save()
                return HttpResponseRedirect(reverse('poll'))
            else :
                return render(request, 'add_leave.html', {'form1': form1})

    form1= LeaveForm()
    return render(request, 'add_leave.html', {'form1': form1})


def leave_list(request):
    leave = Leave.objects.all()
    filter=LeaveFilter(request.POST,queryset=leave)
    leave=filter.qs
    return render(request, 'leave_list.html', {'leaves':leave,'filter':filter})  


def update_leave(request,pk):
    leave=Leave.objects.get(id=pk)
    if request.method=='POST':
        form1=LeaveForm(request.POST,instance=leave)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1=LeaveForm(instance= leave)
    return render(request, 'update_leave.html', {'form1': form1}  )   


def delete_leave(request,pk):
    leave=Leave.objects.get(id=pk)
    if request.method=='POST':
        leave.delete()
        return HttpResponseRedirect(reverse('poll'))
    form1=LeaveForm(instance= leave)
    return render(request, 'delete_leavel.html', {'form1': form1}  )  


def add_dept(request):
    if request.method == 'POST':
            form1=DepartmentForm(request.POST)
            if form1.is_valid():
                form1.save()
                return HttpResponseRedirect(reverse('poll'))
    form1= DepartmentForm()
    return render(request, 'add_employee.html', {'form1': form1})


def department_list(request):
    department= Department.objects.all()
    filter=DepartmentFilter(request.POST,queryset=department)
    department=filter.qs
    return render(request, 'department_list.html', {'department':department,'filter':filter})  

       
def update_dept(request,pk):
    dept=Department.objects.get(id=pk)
    if request.method=='POST':
        form1=DepartmentForm(request.POST,instance=dept)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1=DepartmentForm(instance= dept)
    return render(request, 'update_dept.html', {'form1': form1}  )  


def delete_dept(request,pk):
    dept=Department.objects.get(id=pk)
    if request.method=='POST':
         dept.delete()
         return HttpResponseRedirect(reverse('poll'))
    form1=DepartmentForm(instance= dept)
    return render(request, 'delete_dept.html', {'form1': form1}  )  


def add_pos(request):
    if request.method == 'POST':
        form1=PositionForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1= PositionForm()
    return render(request, 'add_pos.html', {'form1': form1}  ) 


def update_pos(request,pk):
    pos=Position.objects.get(id=pk)
    if request.method=='POST':
        form1=PositionForm(request.POST,instance=pos)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1=PositionForm(instance= pos)
    return render(request, 'update_pos.html', {'form1': form1}  )  


def delete_pos(request,pk):
    pos=Position.objects.get(id=pk)
    if request.method=='POST':
        pos.delete()
        return HttpResponseRedirect(reverse('poll'))
    form1=PositionForm(instance=pos)
    return render(request, 'delete_pos.html', {'form1': form1}  )  


def position_list(request):
    pos= Position.objects.all()
    filter=PositionFilter(request.POST,queryset=pos)
    pos=filter.qs
    return render(request, 'position_list.html', {'positions':pos,'filter':filter})  


def add_sal(request):
    if request.method == 'POST':
        form1=SalaryForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1= SalaryForm()
    return render(request, 'add_sal.html', {'form1': form1}  )   


def update_sal(request,pk):
    sal=Salary.objects.get(id=pk)
    if request.method=='POST':
        form1=SalaryForm(request.POST,instance=sal)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('poll'))
    form1=SalaryForm(instance=sal)
    return render(request, 'update_sal.html', {'form1': form1}  )  
    

def delete_sal(request,pk):
    sal=Salary.objects.get(id=pk)
    if request.method=='POST':
        sal.delete()
        return HttpResponseRedirect(reverse('poll'))
    form1=SalaryForm(instance= sal)
    return render(request, 'delete_sal.html', {'form1': form1}  )  


def salary_list(request):
    salary=Salary.objects.all()
    filter=SalaryFilter(request.POST,queryset=salary)
    salary=filter.qs
    return render(request, 'salary_list.html', {'salary':salary,'filter':filter})  















