__author__ = 'jsmorrison'
from dnd.management.config import config

from django.core.management.base import BaseCommand
from ...models import CharacterNew

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.config_to_db()

    def config_to_db(self):
        for key, val in config.my_character_dict.items():
            (dnd_instance, new_character) = CharacterNew.objects.update_or_create(
                name = key,
                color = val['color'],
                experience=val['exp'],
                char_class=val['class'],
                race=val['race'],
                level=val['level'],
                background=val['background'],
                alignment=val['alignment'],
                hp=val['hp'],
                hit_die=val['hit_die'],
                ac=val['ac'],
                speed=val['speed'],
                prof_bonus=val['prof_bonus'],
                passive_perception=val['passive_perception'],
                str_ability=val['stats'][0],
                dex_ability=val['stats'][1],
                con_ability=val['stats'][2],
                int_ability=val['stats'][3],
                wis_ability=val['stats'][4],
                char_ability=val['stats'][5],
                saving_throw=val['saving_throw'],
                proficiencies=val['proficiencies'],
                armor=val['armor'],
                weapon=val['weapon'],
                spells=val['spells'],
                cantrip=val['cantrip'],
                level_1=val['level_1'],
                level_2="",
                level_3="",
                level_4="",
                level_5="",
                level_6="",
                level_7="",
                level_8="",
                level_9="",
                other="",
            )