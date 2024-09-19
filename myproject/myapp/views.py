from django.shortcuts import render
from . models import ABOUT, DOCTORS

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    about = ABOUT.objects.get()
    return render(request, 'about.html', {'about':about})

def Departments(request):
    return render(request, 'departments.html')

def Doctors(request):
    doctors = DOCTORS.objects.all()
    return render(request, 'doctors.html', {'doctors':doctors})

def Contact(request):
    return render(request, 'contact.html')