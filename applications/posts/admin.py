from django.contrib import admin
from .models import Article, Section, Subsection, Title

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'orden', 'app') 
    ordering = ('orden',)

admin.site.register(Article)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection)
admin.site.register(Title)

