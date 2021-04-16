from django.shortcuts import render
from . import models

# Create your views here.
def menu_show(request):
    item= models.Menu.objects.all()
    return render(request,'menus/menu.html',{'items':item})
