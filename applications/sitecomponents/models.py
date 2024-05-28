from django.db import models
from django.apps import apps


class App(models.Model):
    name = models.CharField(max_length=50)
    icon_name = models.CharField(max_length=50)

    @property
    def ordered_sections(self):
        Section = apps.get_model('posts', 'Section')
        return Section.objects.filter(app=self).order_by('orden')

    def __str__(self):
        return self.name