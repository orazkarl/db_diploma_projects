from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import DiplomaProject
class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            diploma_project = get_object_or_404(DiplomaProject, student__user=request.user)
            self.extra_context = {
                'diploma_project': diploma_project
            }
        return super().get(request, *args, **kwargs)