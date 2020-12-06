from django.urls import path,include

from . import views
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]