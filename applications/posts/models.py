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

class Article(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, related_name='articles', null=True)
    orden = models.IntegerField(default=0, null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=False)
    reference = models.TextField(max_length=200, blank=True, null=True) # Opcional

    def delete(self, *args, **kwargs):
        # Eliminar todas las imágenes relacionadas
        for image in self.images.all():
            image.delete()
        # Eliminar todos los archivos relacionados
        for file in self.files.all():
            file.delete()
        # Eliminar todos los videos relacionados
        for video in self.videos.all():
            video.delete()
        super(Article, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Element(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=3000, null=False, blank=False)
    reference = models.TextField(max_length=200, blank=True, null=True) # Opcional
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='elements', null=True)

    def delete(self, *args, **kwargs):
        # Eliminar todas las imágenes relacionadas
        for image in self.images.all():
            image.delete()
        # Eliminar todos los archivos relacionados
        for file in self.files.all():
            file.delete()
        # Eliminar todos los videos relacionados
        for video in self.videos.all():
            video.delete()
        super(Element, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    article = models.ForeignKey('Article', related_name='article_images', on_delete=models.CASCADE, null=True, blank=True)
    element = models.ForeignKey('Element', related_name='element_images', on_delete=models.CASCADE, null=True, blank=True)

class File(models.Model):
    name = models.CharField(null=True, blank=False, max_length=200, verbose_name='Nombre (obligatorio)', unique=True)
    file = models.FileField(upload_to='files/')
    article = models.ForeignKey('Article', related_name='article_files', on_delete=models.CASCADE, null=True, blank=True)
    element = models.ForeignKey('Element', related_name='element_files', on_delete=models.CASCADE, null=True, blank=True)

class Video(models.Model):
    url = models.URLField()
    article = models.ForeignKey('Article', related_name='article_videos', on_delete=models.CASCADE, null=True, blank=True)
    element = models.ForeignKey('Element', related_name='element_videos', on_delete=models.CASCADE, null=True, blank=True)