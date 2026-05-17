from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField('Nombre', max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField('Descripción', blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Post(models.Model):
    DRAFT = 'borrador'
    PUBLISHED = 'publicado'
    STATUS_CHOICES = [
        (DRAFT, 'Borrador'),
        (PUBLISHED, 'Publicado'),
    ]

    title = models.CharField('Título', max_length=250)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    excerpt = models.TextField('Resumen', max_length=500, blank=True, help_text='Breve descripción del artículo')
    content = RichTextUploadingField('Contenido')
    featured_image = models.ImageField('Imagen destacada', upload_to='blog/images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='posts', verbose_name='Categoría')
    tags = TaggableManager('Etiquetas', blank=True)
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default=DRAFT)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)
    published_at = models.DateTimeField('Publicado', null=True, blank=True)

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == self.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
