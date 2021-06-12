from django.contrib import admin
from django.apps import apps
from .models import Competition, Qualification
app = apps.get_app_config('general')

for model_name, model in app.models.items():
    admin.site.register(model)

class QualificationTabularInline(admin.TabularInline):
    model = Qualification

class CompetitionAdmin(admin.ModelAdmin):
    inlines = [QualificationTabularInline]
    model = Competition

admin.site.unregister(Competition)
admin.site.register(Competition, CompetitionAdmin)