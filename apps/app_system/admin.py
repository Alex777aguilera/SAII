from django.contrib import admin

from django.apps import apps

myapp = apps.get_app_config("app_system")

for model_name, model in myapp.models.items():
	admin.site.register(model)