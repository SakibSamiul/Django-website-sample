from django.shortcuts import render
from . models import ABOUT, DOCTORS, DEPARTMENTS

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    about = ABOUT.objects.get()
    return render(request, 'about.html', {'about':about})

def Departments(request):
    departments = DEPARTMENTS.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def Doctors(request):
    doctors = DOCTORS.objects.all()
    return render(request, 'doctors.html', {'doctors':doctors})

def Contact(request):
    return render(request, 'contact.html')