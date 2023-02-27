from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'dashboard/test.html')


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


def istiaq(request):
    return render(request, 'dashboard/istiaq.html')


def rafi(request):
    return render(request, 'dashboard/rafi.html')


def jahedul(request):
    return render(request, 'dashboard/jahedul.html')

def system(request):
    return render(request, 'dashboard/system-Diagram.html')


def hardwere(request):
    return render(request, 'dashboard/hardware-Design.html')

def merge(request):
    return render(request, 'dashboard/merged-summary.html')

def draft(request):
    return render(request, 'dashboard/draft.html')

def survey_form(request):
    return render(request, 'dashboard/survey-form.html')

def survey_ques(request):
    return render(request, 'dashboard/survey-questions.html')