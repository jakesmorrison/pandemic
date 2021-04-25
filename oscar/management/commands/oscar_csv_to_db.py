__author__ = 'jsmorrison'
from dnd.management.config import config

from django.core.management.base import BaseCommand
from ...models import OscarCategories, Winners
import os
import pandas as pd
import datetime

# python manage.py oscar_csv_to_db

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.add_oscar()
        self.add_place_holder_winners()

    def add_oscar(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = dir_path + "/../../static/oscar/csv/Oscars_2021.csv"

        df = pd.read_csv(file_name)
        df.columns = ["Year", "Cat", "Selection"]

        for index, row in df.iterrows():
            year = row["Year"]
            cat = row["Cat"]
            sel = row["Selection"].replace('“','').replace('”','').replace('"','')

            (oscar_instance, oscar) = OscarCategories.objects.update_or_create(
                Year =year,
                Cat = cat,
                Name = sel,
            )

    def add_place_holder_winners(self):
        now = datetime.datetime.now()
        y = str(now.year)

        catarr = {"Best Picture": 3, "Best Actor": 3, "Best Actress": 3, "Best Supporting Actor": 3, "Best Supporting Actress": 3,
                  "Best Director": 3, "Best Animated Feature": 3, "Best Animated Short": 1 , "Best Adapted Screenplay": 3, "Best Original Screenplay": 3,
                  "Best Cinematography": 2, "Best Documentary Feature": 2, "Best Live-Action Short Film": 1, "Best International Feature": 2,
                  "Best Film Editing": 2, "Best Sound": 2, "Best Production Design": 2,
                  "Best Original Score": 2, "Best Original Song": 2, "Best Hair and Makeup": 2, "Best Costume Design": 2, "Best Visual Effects": 2,
                  "Best Documentary Short Subject": 1}

        for key,val in catarr.items():
            (oscar_instance, oscar) = Winners.objects.update_or_create(
                Year=y,
                Cat=key,
                Name="NA",
                Weight = val,
            )
