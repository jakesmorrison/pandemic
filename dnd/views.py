from django.shortcuts import render
from dnd.management.config import config
import os
import pickle
import pandas as pd
from django.http import JsonResponse
import json
from bs4 import BeautifulSoup

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = dir_path + "/static/dnd/csv/spells.pickle"
with open(file_name, 'rb') as handle:
    b = pickle.load(handle)


# Create your views here.

def index(request):
    my_character_dict = config.my_character_dict
    my_character_list = sorted(config.my_character_dict.keys())

    context={
        'my_character_list': my_character_list,
        'my_character_dict': my_character_dict,
    }
    return render(request, "dnd/characters.html", context)

def combat(request):
    my_character_dict = config.my_character_dict
    my_character_list = sorted(config.my_character_dict.keys())

    context={
        'my_character_list': my_character_list,
        'my_character_dict': my_character_dict,
    }
    return render(request, "dnd/combat.html", context)

def spells(request):
    temp_1 = []
    for key, val in b.items():
        temp_2 = ["ZZZ"+key+"YYY", "XXX"+val['spell_type']+"WWW", "VVV"+val['level']+"UUU", val['casting_time'], val['range'], val['duration'], ', '.join(val['whose_spell'])]
        temp_1.append(temp_2)
    df = pd.DataFrame(temp_1)
    df.columns = "Spell,Spell Type,Level,Casting Time,Range,Duration,For".split(",")
    df["Spell"] = df["Spell"].apply(lambda x: x.replace("&rsquo;", "'"))

    html_table = df.to_html(index=False, classes= 'table table-striped table-bordered table-hover table-responsive" id = "my_table')

    html_table = html_table.replace("<td>ZZZ","<td> <button onclick='add_card(this)' type='button' class='btn btn-success spell-name'>").replace("YYY</td>","</button></td>")
    html_table = html_table.replace("<td>XXX","<td><button type='button' class='btn btn-default spell-type'>").replace("WWW</td>","</button></td>")
    html_table = html_table.replace("<td>VVV","<td><button type='button' class='btn level'>").replace("UUU</td>","</button></td>")

    context={
        'table': html_table,
    }
    return render(request, "dnd/spells.html", context)

def get_spells(request):
    # val = request.GET["val"]
    # val = val.replace("'", "&rsquo;")
    print("test")
    from dnd.management import methods

    methods.Spells()

    context={
        'data': b[val]
    }
    return JsonResponse(json.loads(json.dumps(context)))
