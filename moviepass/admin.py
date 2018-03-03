from django.contrib import admin

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = "Date,Start,Theater,Movie,Cost,RottenTomatoes,Metacritic,Jake".split(",")
    search_fields = list_display
from .models import Movie
admin.site.register(Movie,MovieAdmin)
