from django.db import models

# Create your models here.
class OscarCategories(models.Model):
    Year = models.IntegerField()
    Cat = models.CharField(max_length=1000)
    Name = models.CharField(max_length=1000)
    def __str__(self):
        return "{} {} {}".format(self.Year,self.Cat,self.Name)