from django.urls import path
from . views import Index, About, Departments, Doctors, Contact

urlpatterns = [
    path('', Index, name='index'),
    path('about', About, name='about'),
    path('departments', Departments, name='departments'),
    path('doctors', Doctors, name='doctors'),
    path('contact', Contact, name='contact'),
]
