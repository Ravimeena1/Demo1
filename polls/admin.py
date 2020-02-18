from django.contrib import admin
from .models import Employee,Salary, Leave, Department,Position
# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Salary)
admin.site.register(Leave)
admin.site.register(Department)