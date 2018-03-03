from django.contrib import admin

# Register your models here.
class OscarCategoriesAdmin(admin.ModelAdmin):
    list_display = "Year,Cat,Name".split(",")
    search_fields = list_display
from .models import OscarCategories
admin.site.register(OscarCategories,OscarCategoriesAdmin)