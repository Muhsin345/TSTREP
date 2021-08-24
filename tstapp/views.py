from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnLogin(request):
    return render(request,'Login.html')
def fnDetails(request):
    return render(request,'Details.html')    
