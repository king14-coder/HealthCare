from django.db import models



class PatientModel(models.Model):
    userid = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)

class DoctorModel(models.Model):
    name= models.CharField(max_length= 30)
    price= models.CharField(max_length= 10)
    description = models.TextField(max_length=500)
    image= models.ImageField(upload_to="media",default="")
    def __str__(self):
        return self.name

class PharmacyModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="media", default="")
    def __str__(self):
        return self.name

class LabModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="media", default="")
    def __str__(self):
        return self.name


