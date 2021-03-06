from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *
import requests
import random
# Create your views here.

def home(request):
	return render(request,"home.html",{})

@csrf_exempt
def register(request):
	response_json={}
	if request.method=='GET':
		return render(request,"index.html",{})
	else:
		for x,y in request.POST.items():
			print("key,value", x, ":", y)
		name=str(request.POST.get('name'))
		password=str(request.POST.get('password'))
		gender=str(request.POST.get('gender'))
		email=str(request.POST.get('email'))
		description=str(request.POST.get('description'))
		city=request.POST['city']
		mobile=int(request.POST.get('mobile'))
		l=login_data(name=name,password=password,gender=gender,email=email,description=description,city=city,mobile=mobile)
		l.save()
		user = User.objects.create_user(username=name, password=password,email=email)
		user.save()
		return render(request,"login.html",{}) 

def loginuser(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        password = request.POST.get('password')
		#print(name)
        user = authenticate(username=name, password=password)
        if user :
            if user.is_active :
                #login(user)
                request.session['user_id'] = user.id
                return render(request, 'test.html', {})
            else:
                return HttpResponse('Welcome')
        else:
            return HttpResponse('Authentication Error')

    else:
        return render(request, 'login.html', {})


def createpage(request):
	if request.method=='POST':
		#print(request.user.id)
		userid = request.session['user_id']
		title=str(request.POST.get('title'))
		body=str(request.POST.get('body'))
		author=str(request.POST.get('author'))
		s=blog_data(title=title,body=body,author_id=userid)
		s.save()
		#user1 = User1.objects.create_user(title=title, body=body,author=author)
		#user1.save()
		return render(request,"test.html",{}) 
	elif request.method == "GET":
		return render(request,"createpost.html",{})




def allpage(request):
		all_post = blog_data.objects.all() # Collect all records from table 
		#print(all_post)
		return render(request,'allpost.html',{'all_post':all_post})

def mypage(request):
	if request.method=='GET':
		userid = request.session['user_id']
		my_post = blog_data.objects.filter(author_id = userid)
		return render(request,'mypost.html',{'my_post':my_post})

def logout(request):
	if request.method=='GET':
		return HttpResponseRedirect("/")

def deletepost(request, data):
	item = blog_data.objects.get(id = data)
	if request.method=='GET':
		userid = request.session['user_id']
		context={'item':item}
		return render(request, 'delete.html', context)
	elif request.method == 'POST':
		item.delete()
		return redirect('mypage')

	
def edit(request, data):
	context = blog_data.objects.get(id=int(data))

	return render(request, 'edit.html', {'edit_data':context})
