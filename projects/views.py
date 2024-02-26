from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

from django.contrib.auth.decorators import login_required



def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/project.html', {'projects': projects})

def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project_obj})

@login_required(login_url = "login")
def createProjects(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form':form
    }
    return render(request,"projects/project_form.html",context)


@login_required(login_url = "login")
def updateProjects(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
     form = ProjectForm(request.POST,request.FILES, instance=project)   
     if form.is_valid():
        form.save()
        return redirect('projects')
    
    context = {
        'form':form
    }
    return render(request,"projects/project_form.html",context)


@login_required(login_url = "login")
def deleteProjects(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    context = {
        'object':project
    }
    return render(request,"projects/delete_object.html",context)
