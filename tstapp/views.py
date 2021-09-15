from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnLogin(request):
    return render(request,'Login.html')
def fnDetails(request):
    return render(request,'Details.html')
def fnUser(request):
    return render(request,'Userhome.html')
def fnFB(request):
    return render(request,'fb345.html')
def fnprdcts(request):
    return render(request,'prdcts.html')    
def fnnav(req):
    return render(req,'nav.html')  
def fngrid(req):
    return render(req,'gridnav.html')
def facebook(req):
    return render(req,'facebook.html')
def navsmpl(req):
    return render(req,'navsmpl.html')
