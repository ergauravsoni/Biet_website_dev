from django.contrib import admin

from django.apps import apps

admin.site.site_header = "BIET Website Administration"

# Register your models here.

models = apps.get_app_config('department').get_models()

for model in models:
    admin.site.register(model)
