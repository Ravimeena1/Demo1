from django.urls import path

from . import views

urlpatterns = [

    path('',views.index, name="poll"),
    path('user_profile',views.user_profile, name="user_profile"),
    path('add/', views.add_employee, name='add-employee'),
    path('leave/', views.add_leave, name='add_leave'),
    path('dept/', views.add_dept, name='add-dept'),
    path('sal/', views.add_sal, name='add-sal'),
    path('pos/', views.add_pos, name='add-pos'),
    path('list_emp/', views.employee_list, name='employee_list'),
    path('salary_list/', views.salary_list, name='salary_list'),
    path('list_dept/', views.department_list, name='department_list'),
    path('position_list/', views.position_list, name='position_list'),
    path('list_leave/', views.leave_list, name='leave_list'),
    path('update_emp/<int:pk>', views.update_emp, name='update_emp'),
    path('delete_emp/<int:pk>', views.delete_emp, name='delete_emp'),
    path('update_dept/<int:pk>', views.update_dept, name='update_dept'),
    path('update_leave/<int:pk>', views.update_leave, name='update_leave'),
    path('update_pos/<int:pk>', views.update_pos, name='update_pos'),
    path('delete_pos/<int:pk>', views.delete_pos, name='delete_pos'),
    path('delete_leave/<int:pk>', views.delete_leave, name='delete_leave'),
    path('update_sal/<int:pk>', views.update_sal, name='update_sal'),
    path('delete_sal/<int:pk>', views.delete_sal, name='delete_sal'),
    path('delete_dept/<int:pk>', views.delete_dept, name='delete_dept'),
]