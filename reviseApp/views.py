from django.shortcuts import render
from reviseApp.models import UserProfile
from reviseApp.forms import UserForm,UserProfileForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'index.html',{'number':100,'text':"Hello World"})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def special(request):
    return HttpResponse("You are logged in!")


def other(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.error,profile_form.error)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'other.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

def user_login(request):
    if request.method=="POST":
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        # user=authenticate(username=username,password=password)
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user=authenticate(username=user_name,password=pass_word)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTVE")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("Invalid")
    else:
        return render(request,'relative_url.html')
