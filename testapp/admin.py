from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmpID', 'EmpPost', 'Photo', 'Age', 'Email', 'Address']
    
    
admin.site.register(Employee, EmployeeAdmin)