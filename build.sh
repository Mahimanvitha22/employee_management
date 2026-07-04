#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate

python manage.py shell << EOF
from django.contrib.auth.models import User
import os
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f'Superuser {username} created.')
else:
    print(f'Superuser {username} already exists.')
EOF
