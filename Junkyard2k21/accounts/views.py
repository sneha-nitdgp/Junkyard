from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from .forms import RegisterForm,TeamForm
from .models import  Team
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.

def index(request):
    return render(request,'accounts/index.html')


def registerview(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                try:
                    team = Team.objects.get(teamname =request.POST['username'] )
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('landing')
                except:
                    return render(request, 'accounts/signup.html', {'form':UserCreationForm(), 'error':'No team exists with this teamname'})
            except IntegrityError:
                return render(request, 'accounts/signup.html', {'form':UserCreationForm(), 'error':'That team has already generated a password..'})
        else:
            return render(request, 'accounts/signup.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginview(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/login.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('landing')
def logoutview(request):
    logout(request)
    return redirect('landing')

    

def teamregistration(request):
	submitted = False
	if request.method == "POST":
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save()
			return 	HttpResponseRedirect('/teamregistration?submitted=True')	
	else:
		form = TeamForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'accounts/teamregistration.html', {'form':form, 'submitted':submitted})

def rules(request):
    return render(request,'accounts/rules.html')

