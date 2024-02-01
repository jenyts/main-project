from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return(self.name)
    
class StudyMaterials(models.Model):
    title=models.CharField(max_length=500,null=True)
    material=models.FileField(upload_to='materials',max_length=500,null=True)
    course=models.ForeignKey(Category,on_delete=models.CASCADE)    
    
    def __str__(self):
        return(self.title)
    
class HomeWorkQtn(models.Model):
    title=models.TextField(primary_key=True)
    course=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return(self.title) 

class HomeWork(models.Model):
    qstn=models.ForeignKey(HomeWorkQtn,on_delete=models.CASCADE)
    ans=models.FileField(upload_to='homework',blank=True)

    def __str__(self):
        return(self.title)

    
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',blank=True,null=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return(self.question)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
