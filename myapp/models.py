from django.db import models

# Create your models here.
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Purpose(models.Model):
    pname=models.CharField(max_length=50)
    
    def __str__(self):
       return self.pname
   
class Form(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    phone=models.IntegerField()
    mail=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose=models.ForeignKey(Purpose,on_delete=models.SET_NULL,blank=True,null=True)
    exampaper=models.BooleanField(default=False)
    textbook=models.BooleanField(default=False)
def __str__(self):
        return self.name