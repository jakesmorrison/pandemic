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
            spell=key.replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            spell_type=val["spell_type"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            level=val["level"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", " "),
            casting_time=val["casting_time"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            range=val["range"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            components=val["components"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            duration=val["duration"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            description=val["description"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
            whose_spell=", ".join(val["whose_spell"]),
            page=val["page"].replace("&rsquo;","'").replace("&#8217;","'").replace("&#039;", "'").replace("&nbsp;", " ").replace("&mdash;", "-").replace("&ndash;", "-"),
        )


dictionary_to_db()



# from dnd.management import methods
# methods.Spells()
