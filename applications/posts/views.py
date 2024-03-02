from django.shortcuts import render, get_object_or_404
from .models import Section, Subsection

def posts(request, section_name):
    current_section = get_object_or_404(Section, name=section_name)
    subsections = Subsection.objects.filter(section=current_section)
    return render(request, 'views/posts.html', {'section': current_section, 'subsections': subsections})

