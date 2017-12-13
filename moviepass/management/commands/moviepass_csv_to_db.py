__author__ = 'jsmorrison'
from django.core.management.base import BaseCommand
from ...models import Movie
import pandas as pd
import numpy as np

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('type')

    def handle(self, *args, **options):
        self.convert_csv_to_db(options['type'])

    def convert_csv_to_db(self, csv_path):
        df = pd.read_csv(csv_path)

        for index, row in df.iterrows():
            date = row["Date"].split("/")
            date = date[2]+"-"+date[0]+"-"+date[1]

            s = Movie(
                Date=date,
                Start =row["Start Time"],
                Theater = row["Theater"],
                Movie = row["Movie"],
                Cost=float(row["Cost"]),
                RottenTomatoes=float(row["Rotten Tomatoes"]),
                Metacritic = float(row["Metacritic"]),
                Jake = row["Jake"]
            )
            s.save()
