from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'dashboard/overview.html')
from django.shortcuts import render
from django.http import  HttpResponse

def about(request):
    return render(request, 'dashboard/about.html')
def pdf(request):
    return render(request, 'dashboard/test.html')

def sadia(request):
    return render(request, 'dashboard/sadia.html')

def mehenaz(request):
    return render(request, 'dashboard/mehenaz.html')

def surem(request):
    return render(request, 'dashboard/surem.html')