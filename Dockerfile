FROM debian:13

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings.production

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    libmariadb-dev \
    pkg-config \
    build-essential \
    apache2 \
    libapache2-mod-wsgi-py3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/blog_papa

COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

RUN mkdir -p staticfiles media

COPY apache/django.conf /etc/apache2/sites-available/django.conf
RUN a2dissite 000-default && \
    a2ensite django && \
    a2enmod wsgi headers

RUN chown -R www-data:www-data /var/www/blog_papa/media

EXPOSE 80

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
