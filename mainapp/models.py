from django.db import models
# from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user_auth.models import User
import numpy as np


class Speciality(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название')
    code = models.CharField(max_length=100, null=True, blank=True, verbose_name='Код')

    def __str__(self):
        return self.name


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='group', verbose_name='Специальность')
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название')

    def __str__(self):
        return self.name

    def get_average(self):
        all_ages = map(lambda x: x.user.get_age(), self.student_set.all())
        avg_age = np.mean(list(all_ages))
        if str(avg_age) == 'nan':
            return 0
        return int(str(avg_age).split(' ')[0])


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.user.username


class DiplomaProject(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Название')
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='diploma_project', verbose_name='Студент')
    description = models.TextField(verbose_name='Описание')
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], null=True, blank=True, verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DiplomaProjectFile(models.Model):
    diploma_project = models.ForeignKey(DiplomaProject, on_delete=models.CASCADE, related_name='diploma_project_file')
    file = models.FileField(null=True, blank=True, upload_to='media/')

    def __str__(self):
        return str(self.file)
