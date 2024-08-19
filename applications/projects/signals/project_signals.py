from django.db.models.signals import post_save
from django.dispatch import receiver
from applications.projects.models import Project


@receiver(post_save, sender=Project)
def assign_unique_name(sender, instance, created, **kwargs):
    if created:  # Comprueba si el objeto acaba de ser creado
        instance.project_name = f"Proyecto Nuevo {instance.id}"
        instance.save()
