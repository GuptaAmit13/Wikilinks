from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from wikilinks.models  import MyUser,Question
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
import random
import urllib
from django.utils import timezone
import os
from mera_code import ghar
import urllib
@csrf_exempt
def get_timeup(request):
	
	return render(request,'timeup.html')

@csrf_exempt
def get_time(request):
    profile_obj=MyUser.objects.get(user=request.user)
    start_time=profile_obj.start
    end_time=profile_obj.end
    diff=end_time-timezone.now()
    diff_seconds=diff.seconds
    return HttpResponse(str(diff_seconds))



# Create your views here.
@csrf_exempt
def home(request):
	if request.method=="GET":
		return render(request,"wikilinks/LoginRegistrationForm/rulespage.html",{})

@csrf_exempt
def return_login(request):
	return render(request,"index.html")

@csrf_exempt
def index(request):
	if request.method=="POST":
		if request.POST['submit']=="login":
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			if user is not None:
				if user.is_active:
					x= User.objects.get(username=user.get_username())
					m= MyUser.objects.get(user=x)
					m.attempt_no=m.attempt_no+1;
					m.start=datetime.now()
					m.end=datetime.now()+timedelta(minutes=15)
					m.save()
					if m.attempt_no>3:
						x.is_active= False
						a={'message':'No of Attempt Exceeded!!','flag':True}
						return render(request,"index.html",a)
					m.level=1
					m.save()
					x.save()
					login(request,user)
					return question(request)
			a={'message':'Invalid Entry or Not Registered Yet','flag':True}
			return render(request,'index.html',a)
		else:
			if User.objects.filter(username= request.POST['usernamesignup']).exists():
				a={'message':'Username already exists!!','flag':True}
				return render(request,"index.html",a)
				
			#if MyUser.objects.filter(user_receiptno=request.POST['youreceipt']).exists():
			#	a={'message':'Receipt number already exists!!','flag':True}
			#	return render(request,"index.html",a)

			else:
				user_name=request.POST.get('usernamesignup')
				user_password=request.POST.get('passwordsignup')
			#	user_receiptno=request.POST.get('youreceipt')
				userstatus=request.POST.get('submit')
				x = User.objects.create_user(username=user_name,password=user_password)
				user=authenticate(username=user_name,password=user_password) 
				login(request,user)
				MyUser.objects.create(user_status=userstatus,user=x,start =datetime.now(), end = (datetime.now() + timedelta(minutes=15)))
				#add user_receiptno=user_receiptno,
				#context={'question_start':question.objects.question_start,'question_end':question.objects.question_end}

				return question(request)
	else:
		return render(request,'index.html')
	
@csrf_exempt
def question(request):
	if request.user.is_authenticated():
		x = User.objects.get(username=request.user)
		m = MyUser.objects.get(user=x)
		q = Question.objects.filter(question_level=m.level)

		l=[]

		for j in q:
			l.append(j)
		r = random.randint(0,len(l)-1)

		m.current = l[r].id
		m.last = l[r].question_start
		m.save() 
		a={'question_start':l[r].question_start,'question_end':l[r].question_end,'level':m.level}
		return render(request,'question.html',a)
	else:
		return HttpResponse("Error")
@csrf_exempt
def game(request):
	if request.user.is_authenticated():
			if request.method=="GET":
				flag=0
				user = User.objects.get(username=request.user)
				m = MyUser.objects.get(user=user)

				q = Question.objects.get(id=m.current)
				path = request.path
				
				
				current = request.GET.get('x')
				if current==None:
					current = path.split('/')[-1]
				print q.question_end
				if q.question_end==current:
					
					m.level += 1
					m.save()

					#for last level
					if m.level >= 6:
						return render(request,"finish.html")
					return question(request)
				print current

				if current=="timeup":
					return render(request,"timeup.html")
				if not os.path.exists("/home/amitgupta/Wiki/wiki/wikilinks/templates/"+current+".html"):

					url = "http://en.wikipedia.org/wiki/"+current
					print url
					try:
						os.system("wget "+url+" -O /home/amitgupta/Wiki/wiki/wikilinks/templates/"+current+".html")
						ghar(current)
						m.last = current
						m.save()
					except:
						return render(request,str(m.last)+".html")
				try:
					return render(request,current+".html")
				except:
					return render(request,str(m.last)+".html")
