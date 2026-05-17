#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=config.settings.production

echo "==> Aplicando migraciones..."
python3 manage.py migrate --noinput

echo "==> Recolectando archivos estáticos..."
python3 manage.py collectstatic --noinput --clear

echo "==> Iniciando Apache..."
exec apache2ctl -D FOREGROUND
