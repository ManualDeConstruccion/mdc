from django.db import models
from applications.sitecomponents.models import App

class Section(models.Model):
    name = models.CharField(max_length=140, unique=True, null=False, blank=False)
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='sections', null=True)
    orden = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name

class Subsection(models.Model):
    name = models.CharField(max_length=140, unique=True, null=False, blank=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subsections')
    orden = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='titles')
    orden = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=3000, null=False, blank=False)
    reference = models.URLField(max_length=200, blank=True, null=True) # Opcional
    images = models.ImageField(upload_to='articles_images/', blank=True, null=True) # Opcional
    video = models.FileField(upload_to='articles_videos/', blank=True, null=True) # Opcional
    files = models.FileField(upload_to='articles_files/', blank=True, null=True) # Opcional
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name