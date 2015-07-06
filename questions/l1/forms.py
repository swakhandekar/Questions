from django import forms
from django.contrib.auth.forms import User
from django import forms
from l1.forms import *
# Create your forms here.

class QuestionForm(forms.Form):
    ques = forms.CharField(max_length=500)
    op1 = forms.CharField(max_length=200)
    op2 = forms.CharField(max_length=200)
    op3 = forms.CharField(max_length=200)
    op4 = forms.CharField(max_length=200)
    radios = forms.RadioSelect()

class StudentForm(forms.Form):
    uname = forms.CharField(max_length=15)
    pword = forms.CharField(max_length=15)
    mail = forms.EmailField()
    fname = forms.CharField(max_length=15)
    lname = forms.CharField(max_length=15)