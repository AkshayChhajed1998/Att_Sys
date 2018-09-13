from django.db import models
from User.models import User
from subject.models import subject
from datetime import datetime
from django.db.models.signals import post_save
    
# Create your models here.
class teacherprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    teacher_id=models.CharField(max_length=7,null=True,unique=False,blank=True,default='')
    image=models.ImageField(upload_to='profilepics/',blank=True,default='')
    mobile_number=models.BigIntegerField(blank=True,default=9999999999)
    department=models.CharField(max_length=40,blank=True,default='')
    last_lecture=models.DateTimeField(blank=True,default=datetime.now)
    dob=models.DateField(blank=True,default=datetime.now)
    address=models.CharField(max_length=100,blank=True,default='')
    years_of_experience=models.PositiveSmallIntegerField(blank=True,default=0)
    education=models.CharField(max_length=50,blank=True,default='')
    subject = models.ManyToManyField(subject,null=True,blank=True)
    
    def __str__(self):
        return self.teacher_id
        
    def save(self,*args,**kwargs):
        super(teacherprofile,self).save(*args,**kwargs)
        print(self)
        if self is not None:
            if self.teacher_id is not '':
                self.user.is_active=True
        return self
        
    
def create_teacherprofile(sender,**kwargs):
    user = kwargs["instance"]
    if user.is_teacher:
        if kwargs["created"] :
            user_profile = teacherprofile(user=user)
            user_profile.save()
        
post_save.connect(create_teacherprofile,sender=User)
        