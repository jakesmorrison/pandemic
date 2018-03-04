from django.contrib import admin
from .models import OscarCategories, Users, Winners

# Register your models here.
admin.site.register(
    OscarCategories,
    list_display="Year,Cat,Name".split(","),
    list_display_links="Year,Cat,Name".split(","),
    search_fields ="Year,Cat,Name".split(","),
)

admin.site.register(
    Winners,
    list_display="Year,Cat,Name,Weight".split(","),
    list_display_links="Year,Cat,Name,Weight".split(","),
    search_fields ="Year,Cat,Name,Weight".split(","),
)

admin.site.register(
    Users,
    list_display="id,Year,User,Cat,Won,Favorite".split(","),
    list_display_links="id,Year,User,Cat,Won,Favorite".split(","),
    search_fields = "id,Year,User,Cat,Won,Favorite".split(","),
)




