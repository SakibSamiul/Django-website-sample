from django.shortcuts import render
from . models import ABOUT

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    about = ABOUT.objects.get()
    return render(request, 'about.html', {'about':about})

def Departments(request):
    return render(request, 'departments.html')

def Doctors(request):
    return render(request, 'doctors.html')

def Contact(request):
    return render(request, 'contact.html')