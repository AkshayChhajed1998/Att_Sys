from django.shortcuts import render,HttpResponseRedirect,redirect,reverse
import teacher.form as forms 
from User.models import User
from attendance_system.err import err
from User.form import GenericCreationForm
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import teacherprofile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
import plotly.offline as py
import plotly.graph_objs as go

app_name='teacher'

# Create your views here.

@login_required()
def edit_Tprofile(request,pk):
    
    if request.user.is_teacher:
        if request.user.pk == pk:
            teacher = User.objects.get(pk=pk)
            Tprofile = teacherprofile.objects.get(user = teacher)
            form = forms.edit(teacher.email,teacher.first_name,teacher.last_name,instance=Tprofile)
            form.fields['last_lecture'].widget.attrs.update()
            if request.method == 'POST':
                form=forms.edit(request.POST["email"],request.POST["first_name"],request.POST["last_name"],request.POST,request.FILES)
                if form.is_valid():
                    fo=form.update(pk)
                    if 'image' in request.FILES:
                        fs=FileSystemStorage()
                        filename=fs.save(request.FILES["image"].name,request.FILES["image"])
                        print(fs.url(filename))
                    return redirect("/"+request.session["type_profile"]+"/dashboard/"+str(pk)+"/")
                else:
                    return HttpResponse("OOOOO")
            else:
                return render(request,'edit.html',{"form" : form})
              
        else:
            return HttpResponse('I')
    else:
        return HttpResponse('II')


def new_teacherform(request):
    
    user_form =GenericCreationForm()
    
    profileinlineformset = inlineformset_factory(User,teacherprofile,fields=('image','mobile_number','department','address','years_of_experience','education','subject','dob','last_lecture'))
    formset = profileinlineformset()
    formset.forms[0].fields['last_lecture'].widget.attrs.update({'class':'datetime'})
    formset.forms[0].fields['dob'].widget.attrs.update({'class':'date'})
    
    if request.method == 'POST':
        user_form = GenericCreationForm(request.POST,request.FILES)
        formset = profileinlineformset(request.POST,request.FILES)
        
        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            created_user.is_teacher=True
            created_user.is_active=False
            formset = profileinlineformset(request.POST,request.FILES,instance=created_user)
            
            if formset.is_valid():
                #fs=FileSystemStorage()
                #filename=fs.save(request.FILES["image"].name,request.FILES["image"])
                created_user.save()
                formset.save()
                #user=authenticate(username=created_user.username,password=created_user.password)
                #if user is not None:
                #    login(request,user)
                #    return redirect('dashboard',pk=user.pk)

                errors=[err(e="Please Reach to Admin and Register Your ID.",link=" "),err(e="Your Account is InActive It will be activated by admin.",link=" ")]
                return render(request,'error.html',{'errors':errors})
    
    return render(request,'signup.html',{
            "pk":None,
            "user_form": user_form,
            "formset": formset,
        
        })

@login_required()
def dashboard_profile(request,pk):
    if request.user.pk == pk:
        teacher=User.objects.get(pk=pk)
        TeacherProfile=teacherprofile.objects.get(user=teacher)
        request.session["profile"]=str(TeacherProfile.image)
        print(request.session["profile"])
        return render(request,'dashboard/profile.html',{'teacher':teacher,'TeacherProfile':TeacherProfile})
    else:
        return HttpResponse("404 bad URL!!!!")
        

@login_required()
def dashboard_analysis(request,pk):
    if request.user.pk == pk:
        teacher=User.objects.get(pk=pk)
        TeacherProfile=teacherprofile.objects.get(user=teacher)
        
        labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
        values = [4500,2500,1053,500]
        colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']

        trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=20),
               marker=dict(colors=colors, 
                           line=dict(color='#000000', width=2)))

        
        div=[py.plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])],include_plotlyjs=False,output_type="div"),py.plot([trace],include_plotlyjs=False,output_type="div")]

        return render(request,'dashboard/analysis.html',{'teacher':teacher,'TeacherProfile':TeacherProfile,'graph':div})
    else:
        return HttpResponse("404 bad URL!!!!")