from django.shortcuts import render
from dnd.management.config import config
import pandas as pd
from django.http import JsonResponse
import json
from dnd.models import Spells, CharacterNew


# Create your views here.

def index(request):
    my_character_dict = {}
    my_character_list = []
    for x in CharacterNew.objects.all().values():
        x["stats"] = [int(x["str_ability"]),int(x["dex_ability"]),int(x["con_ability"]),
                      int(x["int_ability"]),int(x["wis_ability"]),int(x["char_ability"])]
        my_character_dict[x["name"]] = x
        my_character_list.append(x["name"])

    my_character_list = sorted(my_character_list)

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
    my_spells = Spells.objects.all().values()
    temp_1 = []
    for x in range(0,len(my_spells)):
        temp_2 = [my_spells[x]['page'],"ZZZ"+my_spells[x]['spell']+"YYY",
                  "XXX"+my_spells[x]['spell_type']+"WWW", "VVV"+my_spells[x]['level'].replace(" ","")+"UUU",
                  my_spells[x]['casting_time'], my_spells[x]['range'], my_spells[x]['duration'], my_spells[x]['whose_spell']]
        temp_1.append(temp_2)

    df = pd.DataFrame(temp_1)
    df.columns = "Page,Spell,Spell Type,Level,Casting Time,Range,Duration,For".split(",")
    df["Page"] = df["Page"].apply(lambda x: x.replace("from Sword Coast Adventure's Guide", "SCAG").replace("from EE Players Companion","EEPC").replace("from Xanathar's Guide To Everything","XGTE").replace("Players Handbook","PH"))

    html_table = df.to_html(index=False, classes= 'table table-striped table-bordered table-hover table-responsive" id = "my_table')

    html_table = html_table.replace("<td>ZZZ","<td> <button onclick='add_card(this)' type='button' class='btn btn-success spell-name'>").replace("YYY</td>","</button></td>")
    html_table = html_table.replace("<td>XXX","<td><button type='button' data-toggle='tooltip' data-placement='left' title='' class='btn btn-default spell-type'>").replace("WWW</td>","</button></td>")
    html_table = html_table.replace("<td>VVV","<td><button type='button' class='btn level'>").replace("UUU</td>","</button></td>")


    context={
        'table': html_table,
    }
    return render(request, "dnd/spells.html", context)

def get_spells(request):
    val = request.GET["val"]

    context={
        'data': Spells.objects.filter(spell=val).values()[0]
    }
    return JsonResponse(json.loads(json.dumps(context)))
