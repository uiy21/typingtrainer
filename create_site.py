# create_site.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typingtrainer.settings')
django.setup()

from django.contrib.sites.models import Site

site_name = 'localhost'
domain = 'localhost:8000'

site, created = Site.objects.get_or_create(id=1, defaults={'domain': domain, 'name': site_name})
if not created:
    site.domain = domain
    site.name = site_name
    site.save()

print(f'Site with domain {site.domain} and name {site.name} is set.')
