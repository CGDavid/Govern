from django.contrib import admin
from django.apps import apps

apps = apps.get_app_config('projects')

for model_name, model in apps.models.items():
    admin.site.register(model)