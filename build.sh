#!/usr/bin/env bash

# Recolecta estáticos
python manage.py collectstatic --noinput

# Aplica las migraciones
python manage.py migrate --no-input
