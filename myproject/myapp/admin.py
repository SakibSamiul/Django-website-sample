from django.contrib import admin
from . models import ABOUT, DOCTORS, DEPARTMENTS
# Register your models here.
admin.site.register(ABOUT)
admin.site.register(DOCTORS)
admin.site.register(DEPARTMENTS)