from django.urls import path
from . views import Index, About, Departments, Doctors

urlpatterns = [
    path('', Index, name='index'),
    path('about', About, name='about'),
    path('departments', Departments, name='departments'),
    path('doctors', Doctors, name='doctors'),
]
