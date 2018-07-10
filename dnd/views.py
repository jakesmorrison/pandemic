from django.shortcuts import render
# Create your views here.

def index(request):
    my_character_dict = {
        'Joie':{
            'color': '#ff5f5f',
            'class':'Druid',
            'race':'Human',
            'level': '1',
            'background': 'Outlander',
            'alignment': 'Chaotic Good',
            'hp': '12',
            'ac': '14',
            'speed': '30',
            'prof_bonus': '+2',
            'stats': [14,14,18,16,18,12],
            'saving_throw': "Intelligence and Wisdom",
            'proficiencies': "Athletics, Survival",
            'armor': "Light Leather - +1 <br> Wood Shield - +1",
            'weapon': "Club +4 1d8 <br> Dart +4 1d6",
        },
        'Test': {
            'color': '#ff5fff',
            'class': 'Test',
            'race': 'Test',
            'level': '1',
            'background': 'Test',
            'alignment': 'Test',
            'hp': '01',
            'ac': '0',
            'speed': '0',
            'prof_bonus': '0',
            'stats': [10,10,10,10,10,10],
            'saving_throw': "Test",
            'proficiencies': "Test",
            'armor': "Test",
            'weapon': "Test",
        }

    }
    my_character_list = sorted(my_character_dict.keys())

    context={
        'my_character_list': my_character_list,
        'my_character_dict': my_character_dict,
    }
    return render(request, "dnd/characters.html", context)
