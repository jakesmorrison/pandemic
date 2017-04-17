from .. import config as cfg
from django.core.management.base import BaseCommand
from ...models import CityCards,InfectionCards,RolesCard
from geopy.geocoders import Nominatim
import csv
from django.templatetags.static import static


cfg = cfg.Config
class Command(BaseCommand):
    def handle(self, **options):
        self.quick_fix()
    def add_cities(self):
        for x in cfg.cities:
            cc = CityCards(city=x["city"],country=x["country"],population=x["population"],color=x["color"],type=x["type"],connectionCities=x["connectionCities"])
            cc.save()
    def infection_cities(self):
        for x in cfg.infectedCites:
            ic = InfectionCards(city=x["city"],country=x["country"],color=x["color"],type=x["type"])
            ic.save()
    def add_roles(self):
        for x in cfg.roles:
            r = RolesCard(name=x["name"],description=x["description"],color=x["color"],type=x["type"])
            r.save()
    def add_map_coords(self):
        cityInfo = CityCards.objects.all().values()
        geolocator = Nominatim()
        for x in cityInfo:

            city = x["city"]
            country = x["country"]

            lat = -1
            long = -1
            try:
                location = geolocator.geocode(str(city)+", "+str(country))
                lat = location.latitude
                long = location.longitude

            except:
                lat = -1
                long = -1

            savedCity = x
            savedCity["lat"] = lat
            savedCity["long"] = long

            CityCards.objects.filter(city=x["city"]).delete()
            CityCards.objects.create(**savedCity)

    def create_csv(self):
        cityCards = CityCards.objects.all().values()
        cityCSV = []
        for x in cityCards:
            cityCSV.append([x["city"],x["country"],x["color"],x["lat"],x["long"]])

        with open("/Users/jakesmorrison/Dropbox/Pycharm/pandemic/game/static/game/csv/lat_long.csv",  'w', newline='') as f:
            w = csv.writer(f, delimiter=',')
            header = "city,country,color,lat,long".split(",")
            print(header)
            w.writerow(header)
            for data in cityCSV:
                w.writerow(data)

    def quick_fix(self):
        cityCards = CityCards.objects.get(city='San Francisco')
        cityCards.connectionCities = ['Tokyo', 'Manila', 'Los Angeles', 'Chicago']
        cityCards.save()
