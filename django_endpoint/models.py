from  datetime import datetime
from django.db import models
from rest_framework import status
from rest_framework.response import Response

# Create your models here.

def get_today():
    today=datetime.now()
    return today.strftime('%A')

def get_status():
    return Response(status)
    print (status)

class Endpoint(models.Model):
    slack_name= models.CharField(max_length=200)
    #current_day= models.DateTimeField()
    #utc_time=models.DateTimeField(auto_now_add=True)
    track=models.CharField(max_length=200)
    github_file_url=models.CharField(max_length=200)
    github_repo_url=models.CharField(max_length=200)
    status_code= get_status()

def __str__(self):
    return self.name
