# views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import BudgetProject
from .forms import BudgetProjectForm, BudgetSubProjectFormSet


class BudgetProjectCreateView(CreateView):
    model = BudgetProject
    form_class = BudgetProjectForm
    template_name = 'apps/budget/create_budget.html'
    success_url = reverse_lazy('view_budget')  # Asume que hay una URL con este nombre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['subprojects'] = BudgetSubProjectFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['subprojects'] = BudgetSubProjectFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        subprojects = context['subprojects']
        if subprojects.is_valid():
            self.object = form.save()
            subprojects.instance = self.object
            subprojects.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class BudgetProjectDetailView(DetailView):
    model = BudgetProject
    template_name = 'apps/budget/detail_budget.html'
    context_object_name = 'budget'
