from django.urls import path
from .views import BudgetProjectCreateView, BudgetProjectDetailView

app_name = 'budgets'

urlpatterns = [
    path('create/', BudgetProjectCreateView.as_view(), name='create_budget'),
    path('detail/<int:pk>/', BudgetProjectDetailView.as_view(), name='view_budget'),
]
