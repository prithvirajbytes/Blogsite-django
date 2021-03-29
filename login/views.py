from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *
import requests
import random
# Create your views here.
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
		l=login_data.objects.create(name=name,password=password,gender=gender,email=email,description=description,city=city,mobile=mobile)
		return render(request,"login.html",{}) 

def userLogin(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(name=name, password=password)
        if user :
            if user.is_active :
                login(request, user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse('you are not active')
        else:
            return HttpResponse('Your are not a member')

    else:
        return render(request, 'test.html', {})
