from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .form import TeacherProfileDataForm,TeacherProfileDataChangeForm
from .models import teacherprofile

# Register your models here.
class TeacherUserAdmin(admin.ModelAdmin):
    add_form = None
    form = TeacherProfileDataChangeForm
    model = teacherprofile
    list_display = ['user']
    fieldsets=(
            ('Profile',{'fields':('teacher_id','subject','image','mobile_number','department','last_lecture','dob','address','years_of_experience','education')}),
        )
        
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(teacherprofile,TeacherUserAdmin)