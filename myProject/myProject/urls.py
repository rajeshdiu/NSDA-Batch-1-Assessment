
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",signupPage,name="signupPage"),
    path("loginPage",loginPage,name="loginPage"),
    path("dashboard",dashboard,name="dashboard"),
    path("add_jobPage",add_jobPage,name="add_jobPage"),
    path("view_Job_Page",view_Job_Page,name="view_Job_Page"),
    path("logoutPage",logoutPage,name="logoutPage"),
    path("add_jobPage",add_jobPage,name="add_jobPage"),
    
    
    # Job Recruiter
    path("AppliedJobPage",AppliedJobPage,name="AppliedJobPage"),

]
    