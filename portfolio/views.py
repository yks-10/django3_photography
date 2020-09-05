from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Project


def home(request):
    Projects = Project.objects.all()
    return render(request ,'portfolio/home.html', {'projects' : Projects})
