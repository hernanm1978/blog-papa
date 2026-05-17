from django.db import models


class PersonalInfo(models.Model):
    full_name = models.CharField('Nombre completo', max_length=200)
    tagline = models.CharField('Título profesional', max_length=200, blank=True,
                                help_text='Ej: Escritor y ensayista')
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Teléfono', max_length=30, blank=True)
    location = models.CharField('Ubicación', max_length=150, blank=True)
    bio = models.TextField('Sobre mí')
    profile_image = models.ImageField('Foto de perfil', upload_to='cv/', blank=True, null=True)
    linkedin = models.URLField('LinkedIn', blank=True)
    twitter = models.URLField('Twitter / X', blank=True)
    website = models.URLField('Sitio web personal', blank=True)

    class Meta:
        verbose_name = 'Información personal'
        verbose_name_plural = 'Información personal'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # Solo permite un registro
        if not self.pk and PersonalInfo.objects.exists():
            return
        super().save(*args, **kwargs)


class Education(models.Model):
    institution = models.CharField('Institución', max_length=200)
    degree = models.CharField('Título / Carrera', max_length=200)
    field = models.CharField('Especialidad / Área', max_length=200, blank=True)
    start_year = models.PositiveIntegerField('Año de inicio')
    end_year = models.PositiveIntegerField('Año de fin', blank=True, null=True,
                                            help_text='Dejar vacío si está en curso')
    description = models.TextField('Descripción', blank=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Educación'
        verbose_name_plural = 'Educación'
        ordering = ['order', '-start_year']

    def __str__(self):
        return f'{self.degree} — {self.institution}'

    @property
    def period(self):
        end = self.end_year or 'Actualidad'
        return f'{self.start_year} – {end}'


class Experience(models.Model):
    company = models.CharField('Empresa / Organización', max_length=200)
    position = models.CharField('Cargo / Rol', max_length=200)
    start_date = models.DateField('Fecha de inicio')
    end_date = models.DateField('Fecha de fin', blank=True, null=True)
    is_current = models.BooleanField('Trabajo actual', default=False)
    description = models.TextField('Descripción / Logros')
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
        ordering = ['order', '-start_date']

    def __str__(self):
        return f'{self.position} en {self.company}'

    @property
    def period(self):
        end = 'Actualidad' if self.is_current else (self.end_date.strftime('%b %Y') if self.end_date else '')
        return f'{self.start_date.strftime("%b %Y")} – {end}'


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('tecnicas', 'Habilidades técnicas'),
        ('blandas', 'Habilidades blandas'),
        ('otras', 'Otras'),
    ]
    LEVEL_CHOICES = [
        (1, 'Básico'),
        (2, 'Elemental'),
        (3, 'Intermedio'),
        (4, 'Avanzado'),
        (5, 'Experto'),
    ]

    name = models.CharField('Habilidad', max_length=100)
    category = models.CharField('Categoría', max_length=20, choices=CATEGORY_CHOICES, default='tecnicas')
    level = models.PositiveSmallIntegerField('Nivel', choices=LEVEL_CHOICES, default=3)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    @property
    def level_percent(self):
        return self.level * 20


class Language(models.Model):
    LEVEL_CHOICES = [
        ('nativo', 'Nativo'),
        ('avanzado', 'Avanzado (C1/C2)'),
        ('intermedio', 'Intermedio (B1/B2)'),
        ('basico', 'Básico (A1/A2)'),
    ]

    name = models.CharField('Idioma', max_length=100)
    level = models.CharField('Nivel', max_length=20, choices=LEVEL_CHOICES)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['order']

    def __str__(self):
        return f'{self.name} ({self.get_level_display()})'


class Publication(models.Model):
    title = models.CharField('Título', max_length=300)
    publisher = models.CharField('Editorial / Medio', max_length=200, blank=True)
    year = models.PositiveIntegerField('Año')
    url = models.URLField('Enlace', blank=True)
    description = models.TextField('Descripción', blank=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['order', '-year']

    def __str__(self):
        return self.title
