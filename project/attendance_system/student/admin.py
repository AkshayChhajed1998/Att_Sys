from django.contrib import admin
from .models import studentprofile
from .forms import StudentProfileDataForm

class StudentUserAdmin(admin.ModelAdmin):
    form=StudentProfileDataForm
    add_form=None
    
admin.site.register(studentprofile, StudentUserAdmin)
