from django.shortcuts import render
# Create your views here.

def index(request):
    my_character_dict = {
        'Oakley':{
            'color': '#ff5f5f',
            'class':'Druid',
            'race':'Human',
            'level': '1',
            'background': 'Outlander',
            'alignment': 'CG',
            'hp': '12',
            'ac': '15',
            'speed': '30',
            'prof_bonus': '+2',
            'stats': [14,14,18,16,18,12],
            'saving_throw': "Intelligence and Wisdom",
            'proficiencies': "Athletics, Survival",
            'armor': "Leather Armor (11) <br> Wood Shield (+2)",
            'weapon': "Scimitar +4 1d8+2",
            'spells': "Spell Save: 14, Charisma, +6",
            'cantrip': "Poison Spray, Cont ST, 1d12 <br> Guidence",
            'level_1': "Cure Wounds <br> Thunder Wave, Cont ST /2, 2d8",
        },
        'Tarlos Borevain': {
            'color': '#ff5fff',
            'class': 'Rogue',
            'race': 'Halfling (GW)',
            'level': '1',
            'background': 'Outlander',
            'alignment': 'CN',
            'hp': '11',
            'ac': '16',
            'speed': '25',
            'prof_bonus': '2',
            'stats': [11,20,16,12,13,11],
            'saving_throw': "Dexterity, Intelligence",
            'proficiencies': "Acrobatics, Athletics, Insight, Sleight of Hand, Stealth, Survival",
            'armor': "Leather Armor (11)",
            'weapon': "Rapier +7 1d8+5 <br> Shortbow +7 1d6+5",
            'spells': "None",
            'cantrip': "None",
            'level_1': "None",
        }

    }
    my_character_list = sorted(my_character_dict.keys())

    context={
        'my_character_list': my_character_list,
        'my_character_dict': my_character_dict,
    }
    return render(request, "dnd/characters.html", context)
