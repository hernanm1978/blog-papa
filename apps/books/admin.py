from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year', 'is_visible', 'created_at']
    list_filter = ['is_visible', 'published_year']
    search_fields = ['title', 'author', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_visible']
    fieldsets = (
        ('Información del libro', {
            'fields': ('title', 'slug', 'author', 'published_year', 'isbn', 'description')
        }),
        ('Archivos', {
            'fields': ('pdf_file', 'cover_front', 'cover_back')
        }),
        ('Configuración', {
            'fields': ('is_visible',)
        }),
    )
