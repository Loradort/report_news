from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context = {}
   
       
    classes = models.Classes.objects.all().order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'home.html',context)

def genneral(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=1).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'genneral.html',context)

def special_subjects(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=2).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'special_subjects.html',context)

def elective_subjects(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=3).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'elective_subjects.html',context)

def search(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=3).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'elective_subjects.html',context)

def about(request):
    context = {}
   
       
    classes = models.Classes.objects.all().order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'about.html',context)