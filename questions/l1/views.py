from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from l1.models import *
from django import forms
# Create your views here.

@csrf_exempt
def home(request):
    if request.user.is_authenticated():
        d = {'uname': request.user.get_username()}
        return render(request,"logged.html",d)
    else:
        return render(request,"home.html")

@csrf_exempt
def log_in(request):
    if request.user.is_authenticated():
        d = {'uname': request.user.get_username()}
        return render(request,"logged.html",d)
    else:
        if request.method=="POST":
            user=authenticate(username= request.POST['uname'],password = request.POST['pword'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    d = {'uname':request.user.get_username}
                    return render(request,"logged.html",d)

    return render(request,"home.html")

@csrf_exempt
def sign_up(request):
    if request.method=="POST":
        if User.objects.get(username=request.POST['uname']).exists():
            return render(request,"home.html")
        else:
            user = User.objects.create_user(username=request.POST['uname'],
                                            password=request.POST['pword'],
                                            email=request.POST['mail'],
                                            first_name=request.POST['fname'],
                                            last_name=request.POST['lname'])
            student = Student.objects.create(user=user)
            user = authenticate(username=request.POST['uname'],password=request.POST['pword'])
            if user is not None:
                if user.is_active:
                    login(request,user)

            d = {'uname': user.get_username()}
            return render(request,"logged.html",d)
    return render(request,"home.html")

@csrf_exempt
def log_out(requset):
    logout(requset)
    return render(requset,"home.html")

@csrf_exempt
def addques(request):
    if request.user.is_authenticated():
        if request.method == "POST":

            quest = Question.objects.create(user=request.user,title= request.POST['ques'],
                                            op1=request.POST['op1'],
                                            op2=request.POST['op2'],
                                            op3=request.POST['op3'],
                                            op4=request.POST['op4'],
                                            ans=request.POST.get('radios'),
                                            )
            user = User.objects.get(request.user.get_username)
            user.count += 1

            return render(request,"logged.html")
    return render(request,"home.html")

@csrf_exempt
def leaderboard(request):
    users = Student.objects.all().order_by('-upvotes','-count')
    d={'student':users}
    return render(request,'leaderboard.html',d)