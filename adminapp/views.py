from django.shortcuts import render, redirect, reverse, resolve_url
from django.views import generic

from mainapp.models import Group, Speciality, Student, DiplomaProject
from db_diploma_projects.settings import AUTH_USER_MODEL
from .forms import SpecialityForm, GroupForm, StudentUserForm
from django.contrib.auth.forms import UserCreationForm

class AdminIndexView(generic.TemplateView):
    template_name = 'admin/admin.html'


class SpecialityListView(generic.ListView):
    model = Speciality
    template_name = 'admin/speciality_list.html'


class SpecialityCreateView(generic.CreateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'admin/speciality_form.html'

    def get_success_url(self):
        return reverse('speciality_list')

class SpecialityUpdateView(generic.UpdateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'admin/speciality_form.html'

    def get_success_url(self):
        return reverse('speciality_list')


def speciality_delete(request, pk):
    speciality = Speciality.objects.get(id=pk)
    speciality.delete()
    return redirect('/admin/speciality/list')



class GroupListView(generic.ListView):
    model = Group
    template_name = 'admin/group_list.html'


class GroupCreateView(generic.CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'admin/group_form.html'

    def get_success_url(self):
        return reverse('group_list')


class GroupUpdateView(generic.UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'admin/group_form.html'

    def get_success_url(self):
        return reverse('group_list')


def group_delete(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return redirect('/admin/group/list')



class StudentListView(generic.ListView):
    model = Student
    template_name = 'admin/student_list.html'


class StudentCreateView(generic.CreateView):
    model = AUTH_USER_MODEL
    form_class = StudentUserForm
    template_name = 'admin/student_form.html'




    def get_success_url(self):
        return reverse('student_list')


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentUserForm
    template_name = 'admin/student_form.html'

    def get_success_url(self):
        return reverse('student_list')

class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'admin/student_detail.html'

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/admin/student/list')

def diploma_grade(request, pk):
    if request.POST:
        diploma_project = DiplomaProject.objects.get(id=pk)
        grade = request.POST['grade']
        diploma_project.grade = grade
        diploma_project.save()
        return redirect('/admin/student/detail/' + str(diploma_project.student.user.id))

