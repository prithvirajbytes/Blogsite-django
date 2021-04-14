from django.shortcuts import render
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
                return HttpResponse('Authentication Error')
        else:
            return HttpResponse('Welcome')

    else:
        return render(request, 'login.html', {})


	all_post = Post.objects.all()

	my_post = Post.objects.filter(author_id=user.id)

	#return render(request,'test.html,{'all_post':all_post,'my_post':my_post})
