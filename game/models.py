from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.

class CityCards(models.Model):
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    population = models.IntegerField()
    color = models.CharField(max_length=1000)
    type = models.CharField(max_length=100,default="Type 1")
    connectionCities = PickledObjectField(default = [])
    lat = models.FloatField(default=-1)
    long = models.FloatField(default=-1)
    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.city,self.country,self.population,self.color,self.type,self.connectionCities,
                                                self.lat,self.long)

class SpecialEventCards(models.Model):
    name = models.CharField(max_length=1000)
    rules = models.CharField(max_length=1000)
    action = models.CharField(max_length=5000)
    type = models.CharField(max_length=100,default="Type 1")
    def __str__(self):
        return "{} {} {} {}".format(self.name,self.rules,self.action,self.type)

class EmergencyEventCards(models.Model):
    name = models.CharField(max_length=1000)
    rules = models.CharField(max_length=1000)
    action = models.CharField(max_length=5000)
    type = models.CharField(max_length=100,default="Type 1")
    def __str__(self):
        return "{} {} {} {}".format(self.name,self.rules,self.action,self.type)

class EpidemicCards(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    type = models.CharField(max_length=100,default="Type 1")
    def __str__(self):
        return "{} {} {}".format(self.name,self.description,self.type)

class MutationCards(models.Model):
    name = models.CharField(max_length=1000)
    rules = models.CharField(max_length=1000)
    action = models.CharField(max_length=5000)
    type = models.CharField(max_length=100,default="Type 1")
    def __str__(self):
        return "{} {} {} {}".format(self.name, self.rules, self.action,self.type)

class InfectionCards(models.Model):
    city = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    color = models.CharField(max_length=1000)
    type = models.CharField(max_length=100, default="Type 2")
    def __str__(self):
        return "{} {} {} {} {}".format(self.city,self.country,self.color,self.type)

class RolesCard(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="Type 3")
    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.description, self.color, self.type)

class Room(models.Model):
    roomId = models.IntegerField(unique=True)
    createdBy = models.CharField(default="x",max_length=1000)
    numberOfPandemicCards = models.IntegerField()
    numberOfRoleCards = models.IntegerField()
    mutation = models.BooleanField()
    def __str__(self):
        return "{} {} {} {} {}".format(self.roomId,self.createdBy,self.numberOfPandemicCards,self.numberOfRoleCards,self.mutation)

class Game(models.Model):
    gameId = models.IntegerField(unique=True)
    roomId = models.ForeignKey('Room')
    gameStarted = models.BooleanField(default=False)
    users = PickledObjectField(default = [])
    infectionCards = PickledObjectField(default = [])
    infectionDiscards = PickledObjectField(default = [])
    actionCards = PickledObjectField(default = [])
    actionDiscards = PickledObjectField(default = [])
    rollCards = PickledObjectField(default = [])
    blueTokens = models.IntegerField(default = "x")
    blackTokens = models.IntegerField(default = "x")
    redTokens = models.IntegerField(default = "x")
    yellowTokens = models.IntegerField(default = "x")
    purpleTokens = models.IntegerField(default = "x")
    infectionRate = models.IntegerField(default = "x")
    outbreaks = models.IntegerField(default="x")
    blueCure = models.BooleanField(default=False)
    blackCure = models.BooleanField(default=False)
    redCure = models.BooleanField(default=False)
    yellowCure = models.BooleanField(default=False)
    purpleCure = models.BooleanField(default=False)
    mapInfection = PickledObjectField(default = [])
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.gameId,self.roomId,self.gameStarted,self.users,self.infectionCards,self.infectionDiscards,
                                                            self.actionCards,self.actionDiscards,self.rollCards,
                                                            self.blueTokens,self.blackTokens,self.redTokens,self.yellowTokens,
                                                            self.purpleTokens,self.infectionRate,self.outbreaks,self.blueCure,
                                                            self.blackCure,self.redCure,self.yellowCure,self.purpleCure, self.mapInfection)

class Player(models.Model):
    roomId = models.ForeignKey('Room')
    playerId = models.IntegerField(unique=True)
    playerName = models.CharField(default="x",max_length=1000)
    playerCards = PickledObjectField(default = [])
    rollCards = PickledObjectField(default = [])
    color = models.CharField(default="x",max_length=1000)
    currentLocation = models.CharField(default="Atlanta",max_length=1000)
    notes = models.CharField(default="Personal Notes-",max_length=1000)
    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.roomId,self.playerId,self.playerName,self.playerCards,self.rollCards,
                                                self.color,self.currentLocation,self.notes)