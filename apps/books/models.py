from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class Book(models.Model):
    title = models.CharField('Título', max_length=250)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    author = models.CharField('Autor', max_length=200)
    description = RichTextField('Descripción')
    pdf_file = models.FileField('Archivo PDF', upload_to='books/pdfs/')
    cover_front = models.ImageField('Tapa', upload_to='books/covers/', blank=True, null=True,
                                     help_text='Imagen de la tapa del libro (opcional)')
    cover_back = models.ImageField('Contratapa', upload_to='books/covers/', blank=True, null=True,
                                    help_text='Imagen de la contratapa del libro (opcional)')
    published_year = models.PositiveIntegerField('Año de publicación', blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=20, blank=True)
    is_visible = models.BooleanField('Visible', default=True)
    created_at = models.DateTimeField('Cargado', auto_now_add=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'slug': self.slug})
