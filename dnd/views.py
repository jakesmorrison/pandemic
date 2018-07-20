from django.shortcuts import render
from dnd.management.config import config
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
