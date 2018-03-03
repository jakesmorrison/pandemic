from django.db import models

# Create your models here.

class Movie(models.Model):
    Date = models.DateField()
    Start = models.TimeField()
    Theater = models.CharField(max_length=1000)
    Movie = models.CharField(max_length=1000)
    Cost = models.FloatField(default=0)
    RottenTomatoes = models.FloatField()
    Metacritic = models.FloatField()
    Jake = models.CharField(max_length=1000, default='Hate, Meh, Like, Love')

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.Date,self.Start,self.Theater,self.Movie,self.Cost,
                                                self.RottenTomatoes,self.Metacritic, self.Jake)


class OscarCategories(models.Model):
    Year = models.IntegerField()
    Cat = models.CharField(max_length=1000)
    Name = models.CharField(max_length=1000)
    def __str__(self):
        return "{} {} {}".format(self.Year,self.Cat,self.Name)