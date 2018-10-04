from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import temp_attendance
from django.views.decorators.csrf import csrf_exempt
from classes.models import classes
from teacher.models import teacherprofile
from student.models import studentprofile
from datetime import datetime,timedelta
from User.models import User
from django.db.models import Q
from attendance.models import attendance
from subject.models import subject
from STCrelation.models import STCrelation
# Create your views here.
@csrf_exempt
def save1(request):
    print(request.POST)
@csrf_exempt    
def save(request):
    print(request.POST)
    RFID=request.POST['RFID'][1:9]
    print(RFID)
    Class=int(request.POST['class'][0])
    FLAG=int(request.POST['FLAG'][0])
    obj= temp_attendance()
    if FLAG==1:
        teacher_id=teacherprofile.objects.filter(RFID=RFID).values_list('user_id',flat=True)[0]
        if not teacher_id:
            print("not teacher")
        else:
            obj.User = User.objects.filter(id=teacher_id)[0]
            obj.FLAG = True
            obj.Class = classes.objects.get(id=Class)
            obj.save()
            print("save1")
    elif FLAG==0:
        student_id=studentprofile.objects.filter(RFID=RFID).values_list('user_id',flat=True)[0]
        if not student_id:
            print("not stu")
        else:
            obj.User = User.objects.get(pk=student_id)
            obj.FLAG =False
            obj.Class = classes.objects.get(id=Class)
            obj.save()
            print("save2")
    else:
        print("Something Wrong with Card!!!")
    return HttpResponse("Added")
@csrf_exempt    
def Apply(request):
    RFID=request.POST['RFID'][1:9]
    Class=int(request.POST['class'][0])
    FLAG=int(request.POST['FLAG'][0])
    obj= temp_attendance()
    if FLAG==1:
        teacher_id = teacherprofile.objects.filter(RFID=RFID).values_list('user_id',flat=True)[0]
        q=Q(User=teacher_id) & Q(Class=Class) 
        temp_attendance.objects.filter(q).delete()
        for student in temp_attendance.objects.filter(Class=Class):
            O = attendance()
            O.teacher=teacherprofile.objects.get(pk=teacher_id)
            O.student=studentprofile.objects.get(user_id=student.User)
            O.Class=classes.objects.get(pk=Class)
            print(O.teacher)
            print(O.Class)
            O.subject=subject.objects.get(pk=STCrelation.objects.filter(teacher=O.teacher,Class=O.Class).values_list('subject',flat=True)[0])
            O.entry_time = student.date_time
            O.date_time=student.date_time-timedelta(minutes=student.date_time.minute,seconds=student.date_time.second)
            O.save()
            student.delete()
    elif FLAG==0:
        student_id=studentprofile.objects.filter(RFID=RFID).values_list('user_id',flat=True)[0]
        temp_attendance.objects.filter(User=student_id,Class=Class).delete()
    return HttpResponse("hugy")
            
            
            
            
            
            
            
            