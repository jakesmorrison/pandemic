from ..models import Spells
import os
import pickle

def dictionary_to_db():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = dir_path + "/../static/dnd/csv/spells.pickle"
    with open(file_name, 'rb') as handle:
        b = pickle.load(handle)


    for key, val in b.items():
        (spell_instance, new_spell) = Spells.objects.update_or_create(
            spell=key.replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            spell_type=val["spell_type"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            level=val["level"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            casting_time=val["casting_time"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            range=val["range"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            components=val["components"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            duration=val["duration"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            description=val["description"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
            whose_spell=", ".join(val["whose_spell"]),
            page=val["page"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'"),
        )

dictionary_to_db()

