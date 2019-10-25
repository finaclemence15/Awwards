from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    profile_pict = models.ImageField(upload_to = 'images/',null=True)
    bio = models.CharField(max_length =60)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    username = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()    
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()         
class Projects (models.Model):
    title = models.CharField(max_length =40)
    image = models.ImageField(upload_to = 'images/')
    description =  HTMLField()
    profile = models.ForeignKey(Profile,null = True)
    poster = models.ForeignKey(User,on_delete=models.CASCADE , null=True) 
    post_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_projects(self):
        self.save()

    
class Rating(models.Model):
    profile = models.ForeignKey(Profile,null = True)
    project = models.ForeignKey(Projects,null = True)
    design =  models.CharField(max_length =60)
    usability = models.CharField(max_length =60)
    content = HTMLField()
    def __str__(self):
        return self.content