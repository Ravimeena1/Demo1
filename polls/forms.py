from django.forms import ModelForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from polls.models import Department,Leave,Employee,Salary, Position
from django import forms

class CustomSignupForm(SignupForm): 
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model=User   
        fields = ['first_name','last_name']
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    
 

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
    

class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
        exclude=['count']


class EmployeeForm(ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = Employee
        fields = '__all__'
        widgets={'user':forms.HiddenInput()}


       
class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'
    

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'  