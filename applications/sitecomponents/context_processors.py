from .models import App


def apps_processor(request):
    apps = App.objects.all()
    return {'apps': apps}