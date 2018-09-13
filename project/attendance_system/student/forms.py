from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from .models import Student

attributes=()

class StudentProfileDataForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('student_id','image','mobile_number','parents_number','department','semester','dob','address','roll_no','section')