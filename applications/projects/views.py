from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'apps/projects/create_project_form.html'
    success_url = reverse_lazy('projects:project_list')

    def post(self, request, *args, **kwargs):
        print("POST data Project:", request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.project_owner = self.request.user
        self.object.save()
        if self.request.is_ajax():
            return JsonResponse({
                'success': True,
                'project': {
                    'id': self.object.id,
                    'name': self.object.name,
                    'description': self.object.description
                }
            })
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'success': False, 'error': form.errors})
        return super().form_invalid(form)


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


# Vista para editar proyectos
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'apps/projects/project_edit.html'
    context_object_name = 'project'
    success_url = reverse_lazy('projects:project_list')

    def form_valid(self, form):
        form.instance.project_owner = self.request.user
        return super().form_valid(form)


# Vista para eliminar proyectos
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'apps/projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:project_list')
    context_object_name = 'project'
