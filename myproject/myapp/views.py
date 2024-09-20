from django.shortcuts import render, redirect
from .forms import *
from . models import *

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
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'contact.html', {'form':form})