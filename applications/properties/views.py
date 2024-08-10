from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property
from .forms import PropertyForm


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'apps/properties/create_property_form.html'
    success_url = reverse_lazy('properties:list')

    def post(self, request, *args, **kwargs):
        print("POST data Property:", request.POST)
        return super().post(request, *args, **kwargs)


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'apps/properties/properties_list.html'
    context_object_name = 'properties'


class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = Property
    template_name = 'apps/properties/property_detail.html'
    context_object_name = 'property'


class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'apps/properties/property_update.html'
    success_url = reverse_lazy('properties:list')


class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    template_name = 'apps/properties/property_delete.html'
    success_url = reverse_lazy('properties:list')
    context_object_name = 'property'
