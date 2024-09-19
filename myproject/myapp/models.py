from django.db import models

# Create your models here.
class ABOUT(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to= 'ABOUT/')

    def __str__(self):
        return self.title
    
class DEPARTMENTS(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to= 'DEPARTMENTS/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class DOCTORS(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to= 'DOCTORS/', blank=True, null=True)

    def __str__(self):
        return self.name