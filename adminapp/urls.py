from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.AdminIndexView.as_view(), name='admin_index'),
    path('student/list', views.StudentListView.as_view(), name='student_list'),
    path('student/create', views.StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:pk>', views.student_delete, name='student_delete'),
    path('student/detail/<int:pk>', views.StudentDetailView.as_view(), name='student_detail'),

    path('student/diploma/<int:pk>/grade', views.diploma_grade, name='diploma_grade'),


    path('speciality/list', views.SpecialityListView.as_view(), name='speciality_list'),
    path('speciality/create', views.SpecialityCreateView.as_view(), name='speciality_create'),
    # path('speciality/detail/<int:pk>', views.SpecialityDetailView.as_view(), name='speciality_detail'),
    path('speciality/update/<int:pk>', views.SpecialityUpdateView.as_view(), name='speciality_update'),
    path('speciality/delete/<int:pk>', views.speciality_delete, name='speciality_delete'),

    path('group/list', views.GroupListView.as_view(), name='group_list'),
    path('group/create', views.GroupCreateView.as_view(), name='group_create'),
    path('group/update/<int:pk>', views.GroupUpdateView.as_view(), name='group_update'),
    path('group/delete/<int:pk>', views.group_delete, name='group_delete'),

]
