from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    print('projectObj:', projectObj)
    return render(request, 'projects/single-project.html', {'project':projectObj})

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk): #primary key is to track in the form
    project = Project.objects.get(id=pk) #queries object to the updateProject, prefills all of the back end data to the form
    form = ProjectForm(instance=project) #chooses the instace/project that we want to edit in the form
    context = {'form': form}

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project) #shows that the data is going to be sent to the instance and then saves it
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, "projects/project_form.html", context) #rendering template

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
