from django.contrib import admin
from .models import Article, Section, Subsection, Title

admin.site.register(Article)
admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Title)