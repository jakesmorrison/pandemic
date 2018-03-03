from django.shortcuts import render
import pandas as pd
from .models import OscarCategories, Winners, Users
from django.http import JsonResponse
import json

# Create your views here

year = 2018

def oscar(request):
    df = pd.DataFrame.from_records(OscarCategories.objects.all().values())
    df = df[df["Year"]==year]
    cat = df["Cat"].tolist()

    my_dict = {}
    for x in cat:
        my_dict[x] = df[df["Cat"]==x]["Name"].tolist()

    context = {
        'oscar_options': my_dict
    }
    return render(request, "oscar/oscar.html", context)

def check_for_user_data(request):
    params = request.GET
    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))


def add_to_db(request):
    params = request.GET
    df_winners = pd.DataFrame.from_records(Winners.objects.all().values())
    df_winners = df_winners[df_winners["Year"]==year]
    winners_list = df_winners["Cat"].tolist()

    for x in winners_list:
        my_cat = params[x].split("zzz")
        win = my_cat[0]
        fav = my_cat[1]

        u = None
        try:
            u = Users.objects.get(User=params["name"],Year=year,Cat=x)
        except:
            u = None

        if u != None:
            if u.Won == "undefined":
                u.Won = win
                u.Favorite = fav
                u.save()
        else:
            d = Users(User=params["name"], Cat=x, Won=win, Year=year, Favorite=fav)
            d.save()

    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))




