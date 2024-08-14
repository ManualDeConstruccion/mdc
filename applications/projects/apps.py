from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.projects'

    def ready(self):
        import applications.projects.signals.project_signals
