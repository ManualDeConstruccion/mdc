from django.contrib import admin
from .models import Article, Section, Subsection, Element, Image, File, Video

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'orden', 'app') 
    ordering = ('orden',)

class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'orden', 'section') 
    ordering = ('orden',)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Número de campos extra para subir imágenes
    fields = ['image']  # Especifica solo los campos que quieres mostrar

class FileInline(admin.TabularInline):
    model = File
    extra = 1
    fields = ['file', 'name']  # Especifica solo los campos que quieres mostrar

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    fields = ['url']  # Especifica solo los campos que quieres mostrar    

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'orden', 'subsection') 
    ordering = ('orden',)
    inlines = [ImageInline, FileInline, VideoInline]

class ElementAdmin(admin.ModelAdmin):
    inlines = [ImageInline, FileInline, VideoInline]
    list_display = ('name', 'article') 

# Registrar cada modelo una vez
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Element, ElementAdmin)


