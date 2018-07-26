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
            spell=key,
            spell_type=val["spell_type"],
            casting_time=val["casting_time"],
            range=val["range"],
            components=val["components"],
            duration=val["duration"],
            description=val["description"],
            whose_spell=", ".join(val["whose_spell"]),
            page=val["page"],
        )
dictionary_to_db()