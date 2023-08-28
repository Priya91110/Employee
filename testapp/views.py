from django.shortcuts import render, HttpResponse

# Create your views here.

def index(self):
    return HttpResponse("Indexpage")

def contact(self):
    return HttpResponse("contact")