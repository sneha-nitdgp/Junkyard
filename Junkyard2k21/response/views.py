from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, response
from django.contrib.auth.models import User


from .models import Response
from accounts.models import Team

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'response/index.html')

@login_required(login_url='/accounts/login/')
def get_question(request):
    user = User.objects.get(username=request.user.username)
    try:
        response = Response.objects.get(user = request.user)
    except:
        response = Response.objects.create(user = request.user)
    if(request.method == 'POST'):
        #response.user=request.user
        response.response = request.POST["response"] ##Assuming form input name = response
        response.save()
        #profile.curr_round += 1
        #user.save()
        return redirect('get_question')
    else:
        
        return render(request,'response/index.html',{'response':response.response})
    
@login_required(login_url='/accounts/login/')
def question(request):
    return render(request,'response/index.html')
    
    
    
   
   
    
    

