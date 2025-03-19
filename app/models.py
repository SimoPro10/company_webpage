from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class GeneralInfo (models.Model):
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    open_hours = models.CharField(max_length=200, blank=True, null=True)
    video_url = models.CharField(max_length=200, blank=True, null=True)
    facebook_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    twitter_url = models.CharField(max_length=200, blank=True, null=True)
    linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    
class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=500,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    user_image = models.CharField(max_length=250,blank=True,null=True)
    stars_count = [
        (1,'one'),
        (2,'two'),
        (3,'three'),
        (4,'four'),
        (5,'five'),
    ]
    rating_count = models.IntegerField(choices=stars_count)
    username = models.CharField(max_length=100)
    user_job_title = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return f"{self.username}-{self.user_job_title}"
    
class FrequentlyAskedQuestions (models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
class ContactFormLog(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100)
    joined_at = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
        return self.first_name
    

class Blog(models.Model):
    blog_image = models.CharField(max_length=250,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)   
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title