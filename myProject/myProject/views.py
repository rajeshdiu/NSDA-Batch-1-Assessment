from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from myApp.models import *
from django.contrib.auth.decorators import login_required

from myApp.models import User

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        display_name = request.POST.get('display_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.display_name = display_name
        user.user_type = user_type
        user.save()

        login(request, user)

        return redirect('loginPage') 
    else:
        return render(request,'signup.html')


def loginPage(request):
    
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')  # Redirect to the user's dashboard
        else:
            # Display an error message for invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Display login form
        return render(request, 'login.html')

@login_required
def dashboard(request):
    user = request.user

    if user.is_authenticated:
        if user.user_type == 'recruiter':
            context = {
                'recruiter_info':'Recruiter-specific information'
                    }
            template_name = 'Recruiter/dashboard.html'
            
        elif user.user_type == 'job_seeker':
            context = {
                'job_seeker_info': 'Job Seeker-specific information'
                }
            template_name = 'JobSeeker/dashboard.html'
        else:
            return render(request, 'invalid_user_type.html')
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('loginPage')

    return render(request, template_name, context)

@login_required
def add_jobPage(request):
    
    if request.method =='POST':
        title=request.POST.get('title')
        category=request.POST.get('category')
        openings=request.POST.get('openings')
        description=request.POST.get('description')
        skills_required=request.POST.get('skills_required')
        
        job=addJobModel(
            title=title,
            category=category,
            openings=openings,
            description=description,
            skills_required=skills_required,
        )
        
        job.save()
        
        return redirect("view_Job_Page")
        
    
    return render(request,'Recruiter/addJob.html')

@login_required
def view_Job_Page(request):
    jobs = addJobModel.objects.all()
    user = request.user

    if user.is_authenticated:
        if user.user_type == 'recruiter':
            template_name = 'Recruiter/viewJob.html'
        elif user.user_type == 'job_seeker':
            template_name = 'JobSeeker/viewjob.html'
        else:
            return render(request, 'invalid_user_type.html')  # Handle other user types as needed
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('loginPage')

    context = {'jobs': jobs}
    return render(request, template_name, context)



def logoutPage(request):
    
    logout(request)
    
    return redirect("loginPage")


@login_required
def AppliedJobPage(request):
    
    
    return render(request,'JobSeeker/AppliedJob.html')
    

