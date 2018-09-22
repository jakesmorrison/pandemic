from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

# class CharacterNew(models.Model):
#     name = models.CharField(max_length=10000, default='x')
#     color = models.CharField(max_length=10000, default="x")
#     experience = models.CharField(max_length=10000, default="x")
#     char_class = models.CharField(max_length=10000, default="x")
#     race = models.CharField(max_length=10000, default="x")
#     level = models.CharField(max_length=10000, default="x")
#     background = models.CharField(max_length=10000, default="x")
#     alignment = models.CharField(max_length=10000, default="x")
#     hp = models.CharField(max_length=10000, default="x")
#     hit_die = models.CharField(max_length=10000, default="x")
#     ac = models.CharField(max_length=10000, default="x")
#     speed = models.CharField(max_length=10000, default="x")
#     prof_bonus = models.CharField(max_length=10000, default="x")
#     passive_perception = models.CharField(max_length=10000, default="x")
#     str_ability = models.CharField(max_length=10000, default="x")
#     dex_ability = models.CharField(max_length=10000, default="x")
#     con_ability = models.CharField(max_length=10000, default="x")
#     int_ability = models.CharField(max_length=10000, default="x")
#     wis_ability = models.CharField(max_length=10000, default="x")
#     char_ability = models.CharField(max_length=10000, default="x")
#     saving_throw = models.CharField(max_length=10000, default="x")
#     proficiencies = models.CharField(max_length=10000, default="x")
#     armor = models.CharField(max_length=10000, default="x")
#     weapon = models.CharField(max_length=10000, default="x")
#     spells = models.CharField(max_length=10000, default="x")
#     cantrip = models.CharField(max_length=100000, default="x")
#     level_1 = models.CharField(max_length=100000, default="x")
#     level_2 = models.CharField(max_length=100000, default="x")
#     level_3 = models.CharField(max_length=100000, default="x")
#     level_4 = models.CharField(max_length=100000, default="x")
#     level_5 = models.CharField(max_length=100000, default="x")
#     level_6 = models.CharField(max_length=100000, default="x")
#     level_7 = models.CharField(max_length=100000, default="x")
#     level_8 = models.CharField(max_length=100000, default="x")
#     level_9 = models.CharField(max_length=100000, default="x")
#     other = models.CharField(max_length=1000000, default="x")
#     def __str__(self):
#         return "{}"
#
# class Spells(models.Model):
#     spell = models.CharField(max_length=10000, default='x')
#     spell_type = models.CharField(max_length=10000, default='x')
#     level = models.CharField(max_length=10000, default='x')
#     casting_time = models.CharField(max_length=10000, default='x')
#     range = models.CharField(max_length=10000, default='x')
#     components = models.CharField(max_length=10000, default='x')
#     duration = models.CharField(max_length=10000, default='x')
#     description = models.CharField(max_length=100000, default='x')
#     whose_spell = models.CharField(max_length=10000, default='x')
#     page = models.CharField(max_length=10000, default='x')
#
#     def __str__(self):
#         return "{} {} {} {} {} {} {} {} {}".format(self.spell, self.spell_type, self.level, self.casting_time, self.range,
#                                                    self.components, self.duration, self.description, self.whose_spell, self.page)
#

class Monster(models.Model):
    name = models.CharField(max_length=10000, default='x')
    size = models.CharField(max_length=10000, default="x")
    type = models.CharField(max_length=10000, default="x")
    alignment = models.CharField(max_length=10000, default="x")
    hp = models.CharField(max_length=10000, default="x")
    ac = models.CharField(max_length=10000, default="x")
    speed = models.CharField(max_length=10000, default="x")
    str_ability = models.CharField(max_length=10000, default="x")
    dex_ability = models.CharField(max_length=10000, default="x")
    con_ability = models.CharField(max_length=10000, default="x")
    int_ability = models.CharField(max_length=10000, default="x")
    wis_ability = models.CharField(max_length=10000, default="x")
    char_ability = models.CharField(max_length=10000, default="x")
    challenge = models.CharField(max_length=10000, default="x")
    xp = models.CharField(max_length=10000, default="x")
    languages = models.CharField(max_length=10000, default="x")
    saving_throw = models.CharField(max_length=10000, default="x")
    skills = models.CharField(max_length=10000, default="x")
    damage_vulnerabilities = models.CharField(max_length=10000, default="x")
    damage_immunities = models.CharField(max_length=10000, default="x")
    condition_immunities = models.CharField(max_length=10000, default="x")
    senses = models.CharField(max_length=10000, default="x")
    actions = models.CharField(max_length=10000, default="x")
    weapon = models.CharField(max_length=10000, default="x")
    spells = models.CharField(max_length=10000, default="x")
    cantrip = models.CharField(max_length=100000, default="x")
    level= models.CharField(max_length=100000, default="x")
    description = models.CharField(max_length=1000000, default="x")
    other = models.CharField(max_length=1000000, default="x")
    def __str__(self):
        return "{}"
