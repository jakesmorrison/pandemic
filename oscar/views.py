from django.shortcuts import render
import pandas as pd
from .models import OscarCategories, Winners, Users
from django.http import JsonResponse
import json
import numpy as np

# Create your views here

year = 2018

def oscar(request):
    df = pd.DataFrame.from_records(OscarCategories.objects.all().values())
    df = df[df["Year"]==year]
    cat = df["Cat"].tolist()


    df_winners = pd.DataFrame.from_records(Winners.objects.all().values())
    df_users = pd.DataFrame.from_records(Users.objects.all().values())

    df_merge = df_users.merge(df_winners, left_on='Cat', right_on='Cat', how='outer')
    del df_merge["Year_x"]
    del df_merge["Year_y"]
    del df_merge["id_x"]
    del df_merge["id_y"]
    del df_merge["Favorite"]
    df_merge = df_merge.reset_index()

    df_merge["Points"] = np.where((df_merge['Won'] == df_merge['Name']), 1*df_merge["Weight"], 0)

    rankings = df_merge.groupby(["User"]).sum().reset_index()
    del rankings["index"]
    del rankings["Weight"]

    rankings = rankings.sort_values(by=['Points'], ascending=False).reset_index()
    rankings["index"] = rankings["index"] + 1
    rankings.columns = ['Rank', 'User', 'Points']

    rankings = rankings.to_html(index=False, classes="rank_table")

    rankings = rankings.replace("<tr>",'<tr class="table_content table-bordered">')
    rankings = rankings.replace('border="1"', "")

    rankings = rankings.replace('<tr style="text-align: right;">','<tr class="table_content">')


    my_dict = {}
    for x in cat:
        my_dict[x] = df[df["Cat"]==x]["Name"].tolist()

    context = {
        'oscar_options': my_dict,
        'rankings': rankings
    }
    return render(request, "oscar/oscar.html", context)

def get_user_picks(request):
    params = request.GET
    user = params["user"]
    df = pd.DataFrame.from_records(Users.objects.all().values())
    df = df[(df["Year"]==year) & (df["User"]==user)]
    df.columns = ['Category', 'Favorite', 'User', 'Winner', 'Year', 'id']
    del df["Year"]
    del df["id"]
    del df["User"]
    df = df[['Category', 'Winner', 'Favorite']]

    table = df.to_html(index=False,classes='table table-striped table-bordered table-hover table-responsive" id="table-custom-sort')

    context = {
        'table': table
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




