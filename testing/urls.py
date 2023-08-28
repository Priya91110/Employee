"""testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("contact/", views.contact),
    path("add_emp/", views.Employee_Form.as_view()),
    path("show_emp/", views.EmployeeList.as_view(), name="show"),
    path("update/<int:pk>/", views.EmployeeUpdate.as_view()),
    path("delete/<int:pk>/", views.EmployeeDelete.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)