from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import Employee
from django.contrib.auth.models import User
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, "testapp/index.html")

def contact(self):
    return HttpResponse("contact")


class Employee_Form(CreateView):
    model = Employee
    fields ="__all__"
    def get_success_url(self):
        return reverse("show")
    
class EmployeeList(ListView):
    model = Employee
    template_name = "testapp/employee_list.html"
    context_object_name = "emp"
    
class EmployeeUpdate(UpdateView):
    model = Employee
    fields = "__all__"
    def get_success_url(self):
        return reverse("show")
    
class EmployeeDelete(DeleteView):
    model = Employee
    def get_success_url(self):
        return reverse("show")
    
def registration(request):
    reg_obj = RegistrationForm()
    if request.method == "POST":
        data = RegistrationForm(request.POST)
        if data.is_valid():
            data = data.save()
            data = data.set_password(data.password)
            data.save()
            return HttpResponseRedirect("/accounts/login/")
    return render(request, "registration/signup.html",{'reg_obj':reg_obj})