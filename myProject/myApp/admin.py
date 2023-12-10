from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'email', 'user_type')
    search_fields = ('username', 'display_name', 'email')
    list_filter = ('user_type',)

admin.site.register(User, UserAdmin)

class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_info')
    search_fields = ('user__username', 'user__display_name')

admin.site.register(RecruiterProfile, RecruiterProfileAdmin)

class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills_set')
    search_fields = ('user__username', 'user__display_name')

admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)


admin.site.register(addJobModel)
