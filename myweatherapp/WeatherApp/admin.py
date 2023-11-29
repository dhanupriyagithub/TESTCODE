from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import City

# Register your models here.
@admin.register(City)
# admin.site.register(City)
class cityResource(ImportExportModelAdmin):
    pass