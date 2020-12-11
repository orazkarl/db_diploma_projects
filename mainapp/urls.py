from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('diploma/create', views.diploma_create, name='diploma_create'),
    path('diploma/update', views.diploma_update, name='diploma_update'),
    path('diploma/delete', views.diploma_delete, name='diploma_delete'),
    path('file/delete/<int:pk>', views.file_delete, name='file_delete'),


]
