from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from l1.models import *
from django import forms
from l1.forms import *
# Create your views here.

@csrf_exempt
def home(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            q = Question.objects.all()
            return render(request, "allquestions.html",{'questions':q})
        else:
            return render(request,"logged.html")

    return render(request,"home.html",{'up_form':True,'in_form':True})

@csrf_exempt
def log_in(request):
    if request.user.is_authenticated():
        return home(request)
    else:
        if request.method=="POST":
            user=authenticate(username= request.POST['uname'],password = request.POST['pword'])
            if user is not None:
                if user.is_active:
                    login(request,user)

                    if request.user.is_staff:
                        q = Question.objects.all()
                        return render(request,"allquestions.html",{'questions':q})
                    return render(request,"logged.html")
    return render(request,"home.html",{'up_form':True,'in_form':False})

@csrf_exempt
def sign_up(request):
    if request.method=="POST":
        if User.objects.filter(username=request.POST['uname']).exists():
            return render(request,"home.html",{'up_form':False,'in_form':True})
        else:

            new_form = StudentForm(request.POST)
            if new_form.is_valid():
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

    return render(request,"home.html",{'up_form':False,'in_form':True})

@csrf_exempt
def log_out(requset):
    logout(requset)
    return home(requset)

@csrf_exempt
def addques(request):
    if request.user.is_authenticated():
        if not request.user.is_staff:
            if request.method == "POST":
                new_form = QuestionForm(request.POST)
                if new_form.is_valid():
                    quest = Question.objects.create(user=request.user,title= request.POST['ques'],
                                                    op1=request.POST['op1'],
                                                    op2=request.POST['op2'],
                                                    op3=request.POST['op3'],
                                                    op4=request.POST['op4'],
                                                    ans=request.POST.get('radios'),
                                                    )
                    u = User.objects.get_by_natural_key(request.user)
                    print u
                    stud = Student.objects.get(user=u)
                    stud.count += 1
                    stud.save()

    return home(request)

@csrf_exempt
def leaderboard(request):
    users = Student.objects.all().order_by('-upvotes','-count')
    d={'student':users}
    return render(request,'leaderboard.html',d)

def my_ques(request):
    if request.user.is_authenticated():
        objects = Question.objects.filter(user=request.user)
        return render(request,"myquestions.html",{'questions':objects})
    return render(request,"home.html",{'up_form':True,'in_form':True})

def question(request):
    if request.user.is_authenticated():
        ques_no = int(request.GET['x'])
        q = Question.objects.get(id=ques_no)
        if q.user == request.user:
            return render(request,"edit.html",{'question':q})
        return render(request,"logged.html")
    return render(request,"home.html",{'up_form':True,'in_form':True})

@csrf_exempt
def save(request):
    if request.user.is_authenticated():
        ques_no = request.POST['id']
        q = Question.objects.get(id=ques_no)
        q.title = request.POST['ques']
        q.op1 = request.POST['op1']
        q.op2 = request.POST['op2']
        q.op3 = request.POST['op3']
        q.op4 = request.POST['op4']
        q.ans = request.POST['radios']

        q.save()
        objects = Question.objects.filter(user=request.user)
        return render(request,"myquestions.html",{'questions':objects})
    return render(request,"home.html",{'up_form':True,'in_form':True})

def delete(request):
    if request.user.is_authenticated():
        ques_id = int(request.GET['x'])
        q = Question.objects.get(id=ques_id)
        if request.user == q.user:
            Question.objects.filter(id=ques_id).delete()
            stud = Student.objects.get(user=request.user)
            stud.count -= 1
            stud.save()
        objects = Question.objects.filter(user=request.user)
        return render(request,"myquestions.html",{'questions':objects})
    return render(request,"home.html",{'up_form':True,'in_form':True})

def staff_view(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            ques_id = int(request.GET['x'])
            q = Question.objects.get(id=ques_id)
            upvoted = Votes.objects.filter(ques=q,te=request.user).exists()
            return render(request,"view_question.html",{'question':q,'upvoted':upvoted})
        return render(request,"logged.html")
    return render(request,"home.html",{'up_form':True,'in_form':True})

def upvote(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            if request.method == "GET":
                ques_id = int(request.GET['x'])
                q = Question.objects.get(id=ques_id)
                Votes.objects.create(ques = q, te=request.user)
                stud = Student.objects.get(user=q.user)
                stud.upvotes += 1
                stud.save()
                return HttpResponseRedirect("/")
        return render(request,"logged.html")
    return render(request,"home.html",{'up_form':True,'in_form':False})