from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100, default='x')
    color = models.CharField(max_length=100, default="x")
    char_class = models.CharField(max_length=100, default="x")
    race = models.CharField(max_length=100, default="x")
    level = models.CharField(max_length=100, default="x")
    background = models.CharField(max_length=100, default="x")
    alignment = models.CharField(max_length=100, default="x")
    hp = models.CharField(max_length=100, default="x")
    ac = models.CharField(max_length=100, default="x")
    speed = models.CharField(max_length=100, default="x")
    Sentence_Count = models.IntegerField(default=0)
    Word_Per_Sentence = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    Unique_Words = models.IntegerField(default=0)
    Average_Unique_Word_Length = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    Vocab_Density = models.FloatField(default=0)
    Unique_Word_list = models.TextField(null=True)
    Occurance_Dict = models.TextField(null=True)
    def __str__(self):
        return "{}".format()

class Spells(models.Model):
    spell = models.CharField(max_length=100, default='x')
    spell_type = models.CharField(max_length=100, default='x')
    casting_time = models.CharField(max_length=100, default='x')
    range = models.CharField(max_length=100, default='x')
    components = models.CharField(max_length=100, default='x')
    duration = models.CharField(max_length=100, default='x')
    description = models.CharField(max_length=100000, default='x')
    whose_spell = models.CharField(max_length=100, default='x')
    page = models.CharField(max_length=100, default='x')

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.spell, self.spell_type, self.casting_time, self.range,
                                                   self.components, self.duration, self.description, self.whose_spell, self.page)

