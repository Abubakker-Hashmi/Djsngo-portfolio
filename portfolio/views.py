from django.shortcuts import render
from django.shortcuts import HttpResponse    #changed
from .models import Project
# Create your views here.
def home(request):
    projects=Project.objects.all()                 #grabbed all elements from database
    return render(request,'portfolio/home.html',{'projects':projects})