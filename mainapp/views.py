from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import DiplomaProject, DiplomaProjectFile


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class IndexView(generic.TemplateView):
    template_name = 'index.html'


@login_required(login_url='/accounts/login/')
def diploma_create(request):
    if request.POST:
        title = request.POST['title']
        description = request.POST['description']
        student = request.user.student
        diploma_project = DiplomaProject.objects.create(title=title, description=description, student=student)
        for file in request.FILES.getlist('file'):
            DiplomaProjectFile.objects.create(diploma_project=diploma_project, file=file)
    return redirect('/')


@login_required(login_url='/accounts/login/')
def diploma_update(request):
    if request.POST:
        title = request.POST['title']
        description = request.POST['description']
        student = request.user.student
        diploma_project = student.diploma_project
        diploma_project.title = title
        diploma_project.description = description
        for file in request.FILES.getlist('file'):
            DiplomaProjectFile.objects.create(diploma_project=diploma_project, file=file)
        return redirect('/')
    return render(request, template_name='update_diploma.html')


@login_required(login_url='/accounts/login/')
def file_delete(request, pk):
    file = DiplomaProjectFile.objects.get(id=pk)
    file.delete()
    return redirect('/diploma/update')


@login_required(login_url='/accounts/login/')
def diploma_delete(request):
    diploma_project = request.user.student.diploma_project
    diploma_project.delete()
    return redirect('/')


