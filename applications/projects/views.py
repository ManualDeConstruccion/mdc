import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm
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


@require_http_methods(["PATCH"])
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    data = QueryDict(request.body).dict()  # Convertir el cuerpo de la solicitud PATCH a un diccionario
    form = ProjectForm(data, instance=project, partial=True)  # Instanciar el formulario con partial=True si usas django-rest-framework
    if form.is_valid():
        form.save()
        return JsonResponse({"message": "Proyecto actualizado correctamente"}, status=200)
    else:
        return JsonResponse({"errors": form.errors}, status=400)


class ProjectCreateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'apps/projects/project_create.html'
    success_url = reverse_lazy('projects:project_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        if pk:
            return get_object_or_404(Project, pk=pk)
        return None  # Retorna None si no hay 'pk', indicando una creación

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Asegurarse de establecer self.object
        if self.object is None:
            # Lógica específica para creación si es necesario
            return self.handle_no_object()
        return super().post(request, *args, **kwargs)

    def handle_no_object(self):
        # Crea un nuevo objeto si es necesario, o redirige
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not self.object:
            self.object = form.save()  # Guarda el nuevo objeto
        else:
            form.save()  # Guarda cambios al objeto existente
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



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
