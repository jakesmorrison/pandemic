from django.shortcuts import render
import pandas as pd
from .models import OscarCategories

# Create your views here

def oscar(request):
    df = pd.DataFrame.from_records(OscarCategories.objects.all().values())
    df = df[df["Year"]==2018]
    cat = df["Cat"].tolist()

    my_dict = {}
    for x in cat:
        my_dict[x] = df[df["Cat"]==x]["Name"].tolist()

    context = {
        'oscar_options': my_dict
    }
    return render(request, "oscar/oscar.html", context)