from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class MyUser(models.Model):
    level = models.IntegerField(default=1)
    user = models.OneToOneField(User)
    #user_receiptno=models.IntegerField(default=000)
    user_status=models.CharField(max_length=10,default="")
    attempt_no=models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    start=models.DateTimeField(default=timezone.now(),blank=False)	
    end = models.DateTimeField(blank=False)
    last = models.CharField(default="",max_length=100)
    def __str__(self):
		return str(self.user)

class Question(models.Model):
    #question_id=models.IntegerField(default=1)	
    question_start=models.CharField(max_length=100,default="")
    question_end=models.CharField(max_length=100,default="")
    question_level=models.IntegerField(default=1)
    def __str__(self):
        return str(self.question_end
            
            )