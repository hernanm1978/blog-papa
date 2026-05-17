from django.views.generic import TemplateView
from .models import PersonalInfo, Education, Experience, Skill, Language, Publication


class CVView(TemplateView):
    template_name = 'cv/cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = PersonalInfo.objects.first()
        context['education'] = Education.objects.all()
        context['experience'] = Experience.objects.all()
        context['skills'] = Skill.objects.all()
        context['languages'] = Language.objects.all()
        context['publications'] = Publication.objects.all()
        return context
