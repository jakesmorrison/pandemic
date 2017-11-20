from django.shortcuts import render
from .models import CreditStatus, PointsUsed

import pandas as pd
import datetime
# Create your views here.

def index(request):
    df_status = pd.DataFrame(list(CreditStatus.objects.all().values()))
    df_used = pd.DataFrame(list(PointsUsed.objects.all().values()))
    df_used = df_used.sort('date').reset_index()


    df_issuer_count = df_status.groupby(["issuer"]).count().reset_index()
    df_issuer_count = df_issuer_count[["issuer","bonus"]]

    df_issuer_points = df_status.groupby(["issuer"]).sum().reset_index()

    cumlative_points = []
    flags = []
    for index, row in df_used.iterrows():
        d = str(row["date"]).split("-")
        date = int(datetime.datetime(int(d[0]), int(d[1]), int(d[2]), 0, 0).timestamp())*1000
        if(index == 0):
            cumlative_points.append({'name':row["where"],'x':date,'y':row["point_cost"]})
            flags.append({'x': date, 'title': 'C', "text": 'Stocks fall on Greece, rate concerns; US dollar dips'})
        else:
            cumlative_points.append({'name':row["where"],'x':date,'y':cumlative_points[index-1]['y']+row["point_cost"]})
            flags.append({'x': date, 'title': 'C', "text": 'Stocks fall on Greece, rate concerns; US dollar dips'})


    context={
        'point_cost':(format (df_used["point_cost"].sum(), ',d')),
        'dollar_cost': (format (df_used["dollar_cost"].sum(), ',d')),
        'points_accum': (format (df_status["bonus"].sum()+df_status["line"].sum(), ',d')),
        'total_cards': df_issuer_count["bonus"].sum(),
        'cat_issuer':df_issuer_count["issuer"].tolist(),
        'data_issuer': df_issuer_count["bonus"].tolist(),
        'data_issuer_points': [x/1000000 for x in df_issuer_points["bonus"].tolist()],
        'cum_points_data': cumlative_points
    }
    return render(request,'creditcard/index.html',context)
