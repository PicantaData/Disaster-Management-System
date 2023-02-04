from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrganizationForm,VolunteerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('userlogin')

    return render(request, 'userlogin.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['email']).exists():
            messages.error(request, "E-mail already exists.")
            return redirect('register')

        if request.POST['password'] != request.POST['confpassword']:
            messages.error(request, "The passwords entered do not match.")
            return redirect('register')

        if len(request.POST['password']) < 8:
            messages.error(request, "Password length is too short.")
            return redirect('register')

        user = User(first_name=request.POST['name'], username=request.POST['email'], password=request.POST['password'])

        if request.POST['type'] == "volunteer":
            request.session['username'] = user.username
            user.save()
            return redirect('volregister')
        else:
            request.session['username'] = user.username
            user.save()
            return redirect('orgregister')

    return render(request, 'userreg.html')


def volregister(request):
    form = VolunteerForm()
    user = User.objects.get(username=request.session['username'])
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
                volunteer = form.save(commit=False)
                volunteer.user = user
                volunteer.save()
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'register.html', {'form':form, 'type':'Volunteer'})
    return render(request, 'register.html', {'form':form, 'type':'Volunteer'})



def orgregister(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = OrganizationForm()
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
                form = form.clean()
                org = form.save(commit=False)
                org.user = request.user
                org.save()
                login(request, request.user)
                return render('index')
        else:
            return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form, 'type':'Organization'})



def userlogout(request):
    logout(request)
    return redirect('index')