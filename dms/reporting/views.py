from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
# Create your views here.

def report(request):

    return render(request, 'report.html')

