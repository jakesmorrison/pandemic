from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
class SpellsModelAdmin(admin.ModelAdmin):
    list_display="self.spell, self.spell_type, self.casting_time, self.range, self.components, self.duration," \
                 "self.description, self.whose_spell, self.page".replace(" ","").replace("self.", "").split(",")
    search_fields = list_display

from .models import Spells
admin.site.register(Spells, SpellsModelAdmin)

