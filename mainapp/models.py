from django.db import models
# from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user_auth.models import User


class Speciality(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='group')
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.user.username


class DiplomaProject(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='diploma_project')
    description = models.TextField()
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DiplomaProjectFile(models.Model):
    diploma_project = models.ForeignKey(DiplomaProject, on_delete=models.CASCADE, related_name='diploma_project_file')
    file = models.FileField(null=True, blank=True, upload_to='media/')

    def __str__(self):
        return str(self.file)
