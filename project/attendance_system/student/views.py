from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from django.http import HttpResponse
from User.models import User
from User.form import GenericCreationForm
from django.forms.models import inlineformset_factory
from .models import studentprofile
from attendance_system.err import err
from django import forms
from django.contrib.auth.decorators import login_required
import student.forms as forms 

# Create your views here.
@login_required
def edit_Sprofile(request,pk):
    if request.user.is_student:
        if request.user.pk==pk:
            student=User.objects.get(pk=pk)
            Sprofile=studentprofile.objects.get(user=student)
            form=forms.edit_student(student.email,student.first_name,student.last_name,instance=Sprofile)
            form.fields['subject'].widget.attrs.update({'class':'checkbox'})
            form.fields['dob'].widget.attrs.update({'class':'date'})
            if request.method=='POST':
                form=forms.edit_student(request.POST["email"],request.POST["first_name"],request.POST["last_name"],request.POST,request.FILES)
                if form.is_valid():
                    fo=form.update(pk)
                    if 'image' in request.FILES:
                        fs=FileSystemStorage()
                        filename=fs.save(request.FILES["image"].name,request.FILES["image"])
                    return redirect("/"+request.session["type_profile"]+"/dashboard/profile/"+str(pk)+"/")
                else:
                    return HttpResponse("OOOOO")
            else:
                return render(request,'student/edit.html',{'form':form})

def new_studentform(request):
    user_form=GenericCreationForm()
    profileinlineformset= inlineformset_factory(User,studentprofile,fields=('image','mobile_number','parents_number','department','semester','dob','address','roll_no','batch','Class','subject'),widgets={'subject':forms.CheckboxSelectMultiple(attrs={'class':'checkbox'})})             
    formset=profileinlineformset()
    
    if request.method=='POST':
        user_form=GenericCreationForm(request.POST)
        formset=profileinlineformset(request.POST)
        
        if user_form.is_valid():
            created_user=user_form.save(commit=False)
            created_user.is_student=True
            created_user.is_active=False
            formset = profileinlineformset(request.POST,request.FILES,instance=created_user)
            
            if formset.is_valid():
            
                created_user.save()
                formset.save()
            
                errors=[err(e="Please Reach to Admin and Register Your ID.",link=" "),err(e="Your Account is InActive It will be activated by admin.",link=" ")]
                return render(request,'error.html',{'errors':errors})

    return render(request,'student/signup.html',{"user_form":user_form,"formset":formset,})
 
@login_required
def dashboard_profile(request,pk):
    if request.user.pk == pk:
        student=User.objects.get(pk=pk)
        StudentProfile=studentprofile.objects.get(user=student)
        request.session["profile"]=str(StudentProfile.image)
        return render(request,'student/dashboard/profile.html',{'student':student,'StudentProfile':StudentProfile})
    else:
        return HttpResponse("404 bad url!")
        
@login_required
def dashboard_analysis(request,pk):
    if request.user.pk==pk:
        student=User.objects.get(pk=pk)
        StudentProfile=studentprofile.objects.get(user=student)
        return render(request,'student/dashboard/analysis.html',{'student':student,'StudentProfile':StudentProfile})
    else:
        return HttpResponse("Bad Url!!!")
        