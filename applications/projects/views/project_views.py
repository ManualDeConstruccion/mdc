import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.projects.models import Project
from applications.projects.forms import ProjectForm
from django.urls import reverse


@login_required
def create_and_edit_project(request):
    new_project = Project(
        name="Nuevo Proyecto",
        description="",
        project_owner=request.user,
        is_active=True
    )
    new_project.save()
    return redirect(reverse('projects:create_project', kwargs={'pk': new_project.pk}))


class ProjectCreateView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'apps/projects/project_create.html'
    context_object_name = 'project'

    def get_object(self):
        # Asegúrate de que el ID del proyecto está siendo capturado como 'pk' en la URL
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'apps/projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(project_owner=self.request.user)


# Vista de detalle
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'apps/projects/project_detail.html'
    context_object_name = 'project'


# Vista para eliminar proyectos
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'apps/projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:project_list')
    context_object_name = 'project'
