from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

from django.views import generic
from .models import User

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

def user_logout(request):
    logout(request)
    return redirect('/')

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