from django.db import models
from teacher.models import teacherprofile
#from student.models import studentprofile
#from subject.models import subject

# Create your models here.
class attendance(models.Model):
    date_time = models.DateTimeField(blank=True,auto_now_add=True)
    status = models.CharField(max_length=1,choices=(('P','PRESENT'),('A','ABSENT')),default='A')
    entry_time = models.DateTimeField(blank=True,auto_now_add=True)
    teacher = models.OneToOneField(teacherprofile)
    #student = models.OneToOneField(studentprofile)
    #subject = models.OneToOneField(subject)
    
    def __str__(self):
        return "{0} {1} {2} {3}".format(self.date_time,self.status,self.entry_time,self.teacher.teacher_id)
        
        