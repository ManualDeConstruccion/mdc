from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class BudgetProject(TimeStampedModel):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='budget_projects')
    profesional = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='professional_user')
    client = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='client_user')
    description = models.TextField(_('Description'), null=True, blank=True)
    amount = models.DecimalField(_('Amount'), max_digits=15, decimal_places=2)
    currency = models.CharField(_('Currency'), max_length=3, default='CLP')
    start_date = models.DateField(_('Start date'), null=True, blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    budget_land_area = models.DecimalField(_('Budget land area'), max_digits=8, decimal_places=2, null=True, blank=True)
    land_area_unit = models.CharField(_('Land Area Unit'), max_length=10, default='m²')  # Ejemplo: m², sqft
    price_per_square_unit = models.DecimalField(_('Price per square unit'), max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.project.name} - Budget'

    class Meta:
        verbose_name = _('Budget Project')
        verbose_name_plural = _('Budget Projects')


class BudgetSubProject(TimeStampedModel):
    budget_project = models.ForeignKey(BudgetProject, on_delete=models.CASCADE, related_name='budget_sub_projects')
    description = models.TextField(_('Description'), null=True, blank=True)
    amount = models.DecimalField(_('Amount'), max_digits=15, decimal_places=2)
    currency = models.CharField(_('Currency'), max_length=3, default='CLP')
    start_date = models.DateField(_('Start date'), null=True, blank=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    budget_land_area = models.DecimalField(_('Budget land area'), max_digits=8, decimal_places=2, null=True, blank=True)
    land_area_unit = models.CharField(_('Land Area Unit'), max_length=10, default='m²')  # Ejemplo: m², sqft
    price_per_square_unit = models.DecimalField(_('Price per square unit'), max_digits=15, decimal_places=2, null=True,
                                                blank=True)


class Stage(TimeStampedModel):
    PAYMENT_TRIGGERS = [
        ('date', _('By Date')),
        ('milestone', _('By Milestone')),
    ]

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), null=True, blank=True)
    budget_project = models.ForeignKey(
        'BudgetProject', on_delete=models.CASCADE, related_name='stages')
    budget_sub_project = models.ForeignKey(
        'BudgetSubProject', on_delete=models.CASCADE, related_name='stages', null=True, blank=True)
    due_date = models.DateField(_('Due date'), null=True, blank=True)
    payment_trigger = models.CharField(_('Payment Trigger'), max_length=10, choices=PAYMENT_TRIGGERS, default='date')
    is_payment_required = models.BooleanField(_('Is payment required'), default=False)
    payment_amount = models.DecimalField(_('Payment amount'), max_digits=15, decimal_places=2, null=True, blank=True)
    payment_type = models.CharField(_('Payment Type'), max_length=10, choices=[
        ('fixed', _('Fixed')),
        ('percentage', _('Percentage'))
    ], default='fixed')
    time_frame = models.IntegerField(_('Time Frame (days)'), default=0, help_text=_('Number of days after the start date if by date'))
    payment_percentage = models.DecimalField(_('Payment Percentage'), max_digits=5, decimal_places=2, null=True, blank=True,
                                             help_text=_('Percentage of the total project budget if by percentage'))
    milestone = models.CharField(_('Milestone'), max_length=255, blank=True, null=True, help_text=_('Milestone that triggers the payment'))

    def __str__(self):
        return f'{self.name} - {self.budget_project.name}'

    class Meta:
        verbose_name = _('Stage')
        verbose_name_plural = _('Stages')
