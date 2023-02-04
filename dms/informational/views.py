from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def donate(request):
    return render(request, 'donate.html')

def guidelines(request):
    return render(request, 'guidelines.html')