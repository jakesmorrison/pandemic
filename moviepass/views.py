from django.shortcuts import render
import pandas as pd
from .management import methods
from .models import Movie

# Create your views here.
def moviepass(request):
    # df = pd.read_csv('oscar/static/oscar/csv/oscar.csv')

    df = pd.DataFrame.from_records(Movie.objects.all().values())

    data = []
    for index, row in df.iterrows():
        data.append({'x':row["RottenTomatoes"],'y':row["Metacritic"],'z':row["Cost"],'color': methods.getColor(row["Jake"]),'name':row["Movie"],'theater':row["Theater"],'Jake': row["Jake"]})

    series = [{'data':data}]

    context={
        'series' : series,
    }
    return render(request,"moviepass/moviepass.html",context)

