from django.contrib import admin
from .models import PersonalInfo, Education, Experience, Skill, Language, Publication


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos personales', {
            'fields': ('full_name', 'tagline', 'profile_image', 'bio')
        }),
        ('Contacto', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Redes', {
            'fields': ('linkedin', 'twitter', 'website')
        }),
    )

    def has_add_permission(self, request):
        return not PersonalInfo.objects.exists()


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'order']
    list_editable = ['order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order', 'is_current']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level', 'order']
    list_filter = ['category']
    list_editable = ['level', 'order']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'order']
    list_editable = ['order']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'year', 'order']
    list_editable = ['order']
