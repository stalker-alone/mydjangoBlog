from django.shortcuts import render
from django.shortcuts import HttpResponse
from menues import models

def about(request):
    #return HttpResponse('Hi, Im Jila this website owner!')
    return render(request,'about.html')

def home(request):
        #return HttpRespjjjjonse('Home jj!hiiiiii')
        item= models.Menu.objects.all()
        return render(request,'home.html',{'items':item})
