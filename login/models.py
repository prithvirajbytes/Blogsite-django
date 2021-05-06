from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class login_data(models.Model):
	name=models.CharField(max_length=50,blank=False,null=False)
	mobile=models.IntegerField(default=0)
	city=models.CharField(max_length=10,blank=False,null=False)
	gender=models.CharField(max_length=10,blank=False,null=False)
	email=models.CharField(max_length=50,blank=False,null=False)
	password=models.CharField(max_length=10,null=False,blank=False)
	description=models.CharField(max_length=100,blank=False,null=False)

class blog_data(models.Model):
	title=models.CharField(max_length=500,blank=False,null=False)
	body=models.CharField(max_length=2000,blank=False,null=False)
	author = models.ForeignKey(User,on_delete=models.CASCADE)


	objects = models.Manager()
	#added_by = models.ForeignKey(author)

	
