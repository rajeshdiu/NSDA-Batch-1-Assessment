from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model


class User(AbstractUser):
    USER=[
        ('recruiter', 'Recruiter'),
        ('job_seeker', 'Job Seeker')
    ]
    display_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(choices=USER, max_length=128)

    def __str__(self):
        return self.username

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_info = models.TextField(max_length=128)

    def __str__(self):
        return f"Recruiter Profile for {self.user.username}"

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills_set = models.TextField(max_length=128)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"Job Seeker Profile for {self.user.username}"
    
    
class addJobModel(models.Model):
    
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    openings=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    skills_required=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
