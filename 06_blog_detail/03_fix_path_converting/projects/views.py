from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def detail(request, slug):
    project = get_object_or_404(Project, slug=slug) 
    return render(request, 'projects/detail.html', {'project': project})