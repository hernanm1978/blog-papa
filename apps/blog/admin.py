from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'published_at', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ['status']
    fieldsets = (
        ('Contenido', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image')
        }),
        ('Clasificación', {
            'fields': ('category', 'tags')
        }),
        ('Publicación', {
            'fields': ('status', 'published_at')
        }),
    )
