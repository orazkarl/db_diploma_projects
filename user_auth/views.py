from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, CustomChangePasswordForm
from .models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    error = 'Аккаунт заблокирован'
            else:
                error = 'Неправильный логин или пароль'
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form, 'error': error})

@login_required(login_url='/accounts/login/')
def user_logout(request):
    logout(request)
    return redirect('/')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'account/profile.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.city = request.POST['city']
        user.phone = request.POST['phone']
        user.dob = request.POST['dob']
        user.save()
        return redirect('/accounts/profile/')

@login_required(login_url='/accounts/login/')
def change_password(request):
    error = ''
    if request.method == 'POST':
        form = CustomChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Ваш пароль успешно обновлен!')
        else:
            messages.error(request, 'Please correct the error below.')
            error = 'Пожалуйста, исправьте ошибку ниже.'
    else:
        form = CustomChangePasswordForm(request.user)
    return render(request, 'account/change_password.html', {'form': form, 'error': error}, )
