from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('dashboard')

def info(request):
    return render(request, 'info.html')

def donate(request):
    return render(request, 'donate.html')

def guidelines(request):
    return render(request, 'guidelines.html')