from django.shortcuts import render, redirect, reverse, resolve_url
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from mainapp.models import Group, Speciality, Student, DiplomaProject
from db_diploma_projects.settings import AUTH_USER_MODEL
from .forms import SpecialityForm, GroupForm, StudentUserForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


def is_superuser(user):
    if user.is_superuser:
        return True
    return not user.is_staff


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class AdminIndexView(generic.TemplateView):
    template_name = 'admin/admin.html'


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class SpecialityListView(generic.ListView):
    model = Speciality
    template_name = 'admin/speciality_list.html'


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class SpecialityCreateView(generic.CreateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'admin/speciality_form.html'

    def get_success_url(self):
        return reverse('speciality_list')


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class SpecialityUpdateView(generic.UpdateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'admin/speciality_form.html'

    def get_success_url(self):
        return reverse('speciality_list')


@user_passes_test(is_superuser)
def speciality_delete(request, pk):
    speciality = Speciality.objects.get(id=pk)
    speciality.delete()
    return redirect('/admin/speciality/list')


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class GroupListView(generic.ListView):
    model = Group
    template_name = 'admin/group_list.html'


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class GroupCreateView(generic.CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'admin/group_form.html'

    def get_success_url(self):
        return reverse('group_list')


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class GroupUpdateView(generic.UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'admin/group_form.html'

    def get_success_url(self):
        return reverse('group_list')


@user_passes_test(is_superuser)
def group_delete(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return redirect('/admin/group/list')


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class StudentListView(generic.ListView):
    # model = Student
    template_name = 'admin/student_list.html'
    queryset = Student.objects.filter(user__is_superuser=False)

    def get(self, request, *args, **kwargs):
        if 'sort' in request.GET:
            sortby = str(request.GET['sort']).split('__')
            if sortby[0] != 'group':
                sortby[0] = 'user__' +sortby[0]
            if sortby[0] == 'name':
                sortby[0] = 'user__first_name'
            if sortby[1] == 'top':
                self.queryset = Student.objects.filter(user__is_superuser=False).order_by(sortby[0])
            elif sortby[1] == 'down':
                sortby[0] = '-' + sortby[0]
                self.queryset = Student.objects.filter(user__is_superuser=False).order_by(sortby[0])
            print(sortby)
        return super().get(request, *args, **kwargs)


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class StudentCreateView(generic.CreateView):
    model = AUTH_USER_MODEL
    form_class = StudentUserForm
    template_name = 'admin/student_form.html'

    def get_success_url(self):
        return reverse('student_list')


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentUserForm
    template_name = 'admin/student_form.html'

    def get_success_url(self):
        return reverse('student_list')


@method_decorator([login_required, user_passes_test(is_superuser, login_url='/admin/')], name='dispatch')
class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'admin/student_detail.html'


@user_passes_test(is_superuser)
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/admin/student/list')


@user_passes_test(is_superuser)
def diploma_grade(request, pk):
    if request.POST:
        diploma_project = DiplomaProject.objects.get(id=pk)
        grade = request.POST['grade']
        diploma_project.grade = grade
        diploma_project.save()
        return redirect('/admin/student/detail/' + str(diploma_project.student.user.id))


