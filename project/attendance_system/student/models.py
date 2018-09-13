from django.db import models
from datetime import datetime
from User.models import User

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    student_id=models.CharField(max_length=7,null=True, unique=False,blank=True, default='')
    image=models.ImageField(upload_to='profilepics/',blank=True,default='')
    mobile_number=models.BigIntegerField(blank=True,default=9999999999)
    parents_number=models.BigIntegerField(blank=True,default=9999999999)
    department=models.CharField(max_length=40,blank=True,default='')
    semester=models.PositiveSmallIntegerField(blank=True)
    dob=models.DateField(blank=True,default=datetime.now)
    address=models.CharField(max_length=100,blank=True,default='')
    roll_no=models.CharField(max_length=6,unique=False)
    section=models.CharField(max_length=1,default='')
    
    def __str__(self):
        return self.student_id
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        