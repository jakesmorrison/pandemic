from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class OscarCategories(models.Model):
    Year = models.IntegerField()
    Cat = models.CharField(max_length=1000)
    Name = models.CharField(max_length=1000)
    def __str__(self):
        return "{} {} {}".format(self.Year,self.Cat,self.Name)

# class Winners(models.Model):
#     Year = models.IntegerField()
#     Cat = models.CharField(max_length=1000)
#     Name = models.CharField(max_length=1000, default="")
#     Weight = models.IntegerField()
#     def __str__(self):
#         return "{} {} {} {}".format(self.Year,self.Cat,self.Name,self.Weight)
#
# class Users(models.Model):
#     User = models.CharField(max_length=1000)
#     Selections = PickledObjectField(default=[])
#     def __str__(self):
#         return "{} {}".format(self.User,self.Selections)
