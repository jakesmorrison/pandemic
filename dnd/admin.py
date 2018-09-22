from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.


# class CharacterNewModelAdmin(admin.ModelAdmin):
#     list_display="name,color,experience,char_class,race,level,background,alignment,hp,hit_die,ac,speed,prof_bonus,passive_perception,str_ability,dex_ability," \
#                 "con_ability,int_ability,wis_ability,char_ability,saving_throw,proficiencies,armor,weapon,spells,cantrip,level_1,level_2,level_3,level_4,level_5," \
#                 "level_6,level_7,level_8,level_9,other".split(",")
#     search_fields = list_display
#
# from .models import CharacterNew
# admin.site.register(CharacterNew, CharacterNewModelAdmin)
#
#
#
# class SpellsModelAdmin(admin.ModelAdmin):
#     list_display="self.spell, self.spell_type, self.level, self.casting_time, self.range, self.components, self.duration," \
#                  "self.description, self.whose_spell, self.page".replace(" ","").replace("self.", "").split(",")
#     search_fields = list_display
#
# from .models import Spells
# admin.site.register(Spells, SpellsModelAdmin)
#

class MonsterModelAdmin(admin.ModelAdmin):
    list_display= "name,size,type,alignment,hp,ac,speed,str_ability,dex_ability,con_ability,int_ability,wis_ability,char_ability,"\
                  "challenge,xp,languages,saving_throw,skills,damage_vulnerabilities,damage_immunities,condition_immunities,senses,"\
                  "actions,weapon,spells,cantrip,level,description,other".split(",")
    search_fields = list_display

from .models import Monster
admin.site.register(Monster, MonsterModelAdmin)



