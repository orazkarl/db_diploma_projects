from django.contrib import admin

from .models import Speciality, Group, Student, DiplomaProject, DiplomaProjectFile

admin.site.register(Speciality)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(DiplomaProject)
admin.site.register(DiplomaProjectFile)
