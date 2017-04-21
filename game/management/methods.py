import numpy as np
from ..models import Room, Game, Player, InfectionCards, MutationCards, CityCards, RolesCard
from . import config as cfg
import random

class Pandemic(object):
    def generate_game_id(self, model, parameter):
        roomId = "".join([str(x) for x in np.random.randint(0, 10, size=6)])
        if self.check_game_id(roomId,model, parameter) == False:
            return roomId
        else:
            self.generate_game_id(model, parameter)

    def check_game_id(self, roomId, model, parameter):
        roomIds = [x[parameter] for x in model.objects.values()]
        if roomId in roomIds:
            return True
        else:
            return False

    def add_room(self,roomId,createdBy,mutation,numberOfPandemicCards,numberOfRoleCards):
        r = Room(roomId=roomId,createdBy=createdBy,mutation=mutation,numberOfPandemicCards=numberOfPandemicCards,numberOfRoleCards=numberOfRoleCards)
        r.save()

    def create_update_game(self,roomObj,user):
        if Game.objects.filter(roomId = roomObj):
            u = user
            g = Game.objects.get(roomId=roomObj)
            user = g.users
            user.append(u)
            user = list(set(user))
            g.users = user
            g.save()
        else:
            infectionCards = InfectionCards.objects.all().values()
            actionCards = CityCards.objects.all().values()
            roles = RolesCard.objects.all().values()
            g = Game(gameId=self.generate_game_id(Game, "gameId"), roomId=roomObj, users = [user], infectionCards=infectionCards,
                     infectionDiscards=[],actionCards=actionCards,actionDiscards=[],blueTokens=cfg.Config.maxCubes,
                     blackTokens=cfg.Config.maxCubes,redTokens=cfg.Config.maxCubes,yellowTokens=cfg.Config.maxCubes,
                     purpleTokens=int(cfg.Config.maxCubes/2),infectionRate =0,outbreaks = cfg.Config.outbreaks,rollCards=roles,
                     mapInfection=self.initial_infection())
            g.save()
        return user

    def deal_cards(self,users,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)

        actionCards = list(currentGame.actionCards)
        random.shuffle(actionCards)

        infectonCards = list(currentGame.infectionCards)
        random.shuffle(infectonCards)

        rollCards = list(currentGame.rollCards)
        random.shuffle(rollCards)

        users = users.replace("[","").replace("]","").split(",")
        for user in users:
            p = Player(roomId=roomObj, playerId=self.generate_game_id(Player, "playerId"),playerName=user,
                       playerCards=actionCards[0:4] ,rollCards=rollCards[0:roomObj.numberOfRoleCards], color="x")
            p.save()
            actionCards = actionCards[4:]
            rollCards = rollCards[roomObj.numberOfRoleCards:]

        currentGame.actionCards = actionCards
        actionCards = self.shuffle_action_cards(list(currentGame.actionCards), roomObj.numberOfPandemicCards)
        currentGame.actionCards = actionCards
        currentGame.infectionCards = infectonCards
        currentGame.rollCards = rollCards
        currentGame.gameStarted = "True"
        currentGame.save()

        infectionCardsList = currentGame.infectionCards
        infectionDiscardList = currentGame.infectionDiscards

        mapDict = currentGame.mapInfection
        actions = [2,3,3,1,2,2,0,1,1]
        discardColors = {"blue":0,"black":0,"red":0,"yellow":0}
        for m,x in enumerate(actions):
            card = infectionCardsList.pop(0)
            infectionDiscardList = [card]+infectionDiscardList
            city = card["city"]
            color = card["color"]
            for n,y in enumerate(mapDict):
                if y["city"] == city:
                    discardColors[color] = discardColors[color]+x
                    foo = y
                    if m%3 == 0:
                        foo["purple"] = foo["purple"] + 1
                    foo[color] = foo[color] + x
                    mapDict[n] = foo
                    break

        currentGame.infectionCards = infectionCardsList
        currentGame.infectionDiscards = infectionDiscardList
        currentGame.mapInfection = mapDict
        currentGame.blueTokens = currentGame.blueTokens - discardColors["blue"]
        currentGame.blackTokens = currentGame.blackTokens - discardColors["black"]
        currentGame.redTokens = currentGame.redTokens - discardColors["red"]
        currentGame.yellowTokens = currentGame.yellowTokens - discardColors["yellow"]
        currentGame.purpleTokens = currentGame.purpleTokens -3

        currentGame.save()

    def shuffle_action_cards(self, actionDeck, numPandemic):
        actionDeck = actionDeck+cfg.Config.mutation
        random.shuffle(actionDeck)
        numCards = int(len(actionDeck) / numPandemic)
        new_deck_counts = [numCards] * numPandemic
        # getting number of cards per sub deck.
        for n, x in enumerate(range(len(actionDeck) - numCards * numPandemic)):
            new_deck_counts[n] = new_deck_counts[n] + 1

        first = 0
        last = new_deck_counts[0]
        new_deck  = []
        pand_cards = cfg.Config.virulent_strain
        event_cards = cfg.Config.events
        random.shuffle(pand_cards)
        for n,x in enumerate(new_deck_counts):
            pan_sub = actionDeck[first:last]+[pand_cards[n]]+[event_cards[n]]
            random.shuffle(pan_sub)
            new_deck = new_deck + pan_sub
            first = last
            last = first + x
        return new_deck


    def getcards(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.get(roomId=roomObj,playerName=user)
        return p.playerCards

    def getrolecards(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.get(roomId=roomObj,playerName=user)
        return p.rollCards

    def getactioncards(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        return currentGame.actionCards

    def getactiondiscards(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        return currentGame.actionDiscards


    def discardaction(self,user,roomId,city):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)

        p = Player.objects.get(roomId=roomObj,playerName=user)
        playerCards = p.playerCards
        for n,x in enumerate(playerCards):
            if x["city"]==city:
                discardCity = playerCards.pop(n)
                actionDiscards = currentGame.actionDiscards
                currentGame.actionDiscards = actionDiscards+[discardCity]
                currentGame.save()
                break
        p.playerCards = playerCards
        p.save()

    def getnewcard(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        card = currentGame.actionCards[0]
        currentGame.actionCards = currentGame.actionCards[1:]
        currentGame.save()
        p = Player.objects.get(roomId=roomObj, playerName=user)
        currentCards =  p.playerCards
        p.playerCards = currentCards + [card]
        p.save()

    def getinfectioncards(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        return currentGame.infectionCards


    def getinfectiondiscards(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        return currentGame.infectionDiscards

    def infectionplaytop(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        topCard = currentGame.infectionCards[0]

        discards =[topCard]+currentGame.infectionDiscards
        currentGame.infectionDiscards = discards
        currentGame.save()

        currentGame.infectionCards.pop(0)
        currentGame.save()


    def infectionplaybottom(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        bottomCard = currentGame.infectionCards[-1]

        discards =[bottomCard]+currentGame.infectionDiscards
        currentGame.infectionDiscards = discards
        currentGame.save()

        currentGame.infectionCards.pop(-1)
        currentGame.save()

    def incrementcolor(self,user,roomId,color):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.filter(roomId=roomObj).values()[0]
        tokenCount = currentGame[color + "Tokens"] + 1
        currentGame[color + "Tokens"] = tokenCount
        Game.objects.filter(roomId=roomObj).delete()
        Game.objects.create(**currentGame)

    def decrementcolor(self,user,roomId,color):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.filter(roomId=roomObj).values()[0]
        tokenCount = currentGame[color + "Tokens"] - 1
        currentGame[color + "Tokens"] = tokenCount
        Game.objects.filter(roomId=roomObj).delete()
        Game.objects.create(**currentGame)

    def gettokens(self,user,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        try:
            infectionToken = cfg.Config.infectionRate[currentGame.infectionRate]
        except:
            infectionToken = cfg.Config.infectionRate[-1]
        return {"blueTokens":currentGame.blueTokens,"blackTokens":currentGame.blackTokens,"redTokens":currentGame.redTokens,
                "yellowTokens":currentGame.yellowTokens,"purpleTokens":currentGame.purpleTokens,"infectionRate":infectionToken,
               "outbreaks":currentGame.outbreaks}


    def incrementother(self, user, roomId, indicator):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.filter(roomId=roomObj).values()[0]
        count = currentGame[indicator] + 1
        currentGame[indicator] = count
        Game.objects.filter(roomId=roomObj).delete()
        Game.objects.create(**currentGame)


    def decrementother(self, user, roomId, indicator):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.filter(roomId=roomObj).values()[0]
        count = currentGame[indicator] - 1
        currentGame[indicator] = count
        Game.objects.filter(roomId=roomObj).delete()
        Game.objects.create(**currentGame)

    def changecure(self, user, roomId, cureName):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.filter(roomId=roomObj).values()[0]
        cure = currentGame[cureName]
        if cure == False:
            cure = True
        else:
            cure = False
        currentGame[cureName] = cure
        Game.objects.filter(roomId=roomObj).delete()
        Game.objects.create(**currentGame)

    def getcures(self, user, roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        return {"blueCure":currentGame.blueCure,"blackCure":currentGame.blackCure,"redCure":currentGame.redCure,
                "yellowCure":currentGame.yellowCure,"purpleCure":currentGame.purpleCure}

    def reshuffleinfectiondeck(self, user, roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)

        discards = list(currentGame.infectionDiscards)
        random.shuffle(discards)

        infectionDeck = currentGame.infectionCards

        currentGame.infectionCards = discards + list(infectionDeck)
        currentGame.save()

        currentGame.infectionDiscards = []
        currentGame.save()

    def removerole(self, user, roomId ,role):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.get(roomId=roomObj,playerName=user)
        rollCards = p.rollCards
        if len(rollCards)>1:
            for n,x in enumerate(rollCards):
                if x["name"] == role:
                    rollCards.pop(n)
                    break
            p.rollCards = rollCards
            p.save()

    def getnotes(self, user, roomId):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.get(roomId=roomObj,playerName=user)
        return p.notes

    def savenotes(self, user, roomId, note):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.get(roomId=roomObj,playerName=user)
        allNotes = str(p.notes) + "-" + note
        p.notes = allNotes
        p.save()

    def pickupdiscard(self, user, roomId, city):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)

        cityList = []
        for x in currentGame.actionDiscards:
            if x["city"] == city:
                cityList = x

        p = Player.objects.get(roomId=roomObj,playerName=user)
        cityCards = p.playerCards

        p.playerCards = list(cityCards) + [cityList]
        p.save()

        discards = currentGame.actionDiscards
        for n,x in enumerate(discards):
            if x["city"] == city:
                discards.pop(n)
        currentGame.actionDiscards = discards
        currentGame.save()

    def get_lat_long(self):
        cityCards = CityCards.objects.all().values()
        cityCSV = []
        for x in cityCards:
            cityCSV.append({"name":x["city"],'color': x["color"],"lat":x["lat"],"lon":x["long"]})
        return cityCSV

    def connect_cities(self):
        cityCards = CityCards.objects.all().values()
        all_lines = []
        for x in cityCards:
            for y in x["connectionCities"]:
                y = CityCards.objects.get(city=y)
                if( (x["city"] == "San Francisco" and (y.city == "Tokyo" or y.city == "Manila")) or (x["city"] == "Los Angeles" and y.city == "Sydney")):
                    pass
                elif ( (x["city"] == "Tokyo" and y.city == "San Francisco") or (x["city"] == "Manila" and y.city == "San Francisco") or (x["city"] == "Sydney" and y.city == "Los Angeles")):
                    pass
                else:
                    all_lines.append({'type': 'mappoint', 'lineWidth': 3, 'lineColor': 'white', 'data':[{'id':x["city"],'color':x["color"],'lat':x['lat'],'lon':x['long']},
                                                                                       {'id':y.city,'color':y.color,'lat':y.lat,'lon': y.long}]})

        return all_lines

    def initial_infection(self):
        cityCards = CityCards.objects.all().values()
        allInfections = []
        for x in cityCards:
            if x['city'] == "Atlanta":
                allInfections.append({'city': x['city'],'researchCenter': True,'blue': 0,'black': 0,'purple': 0,'red': 0,'yellow': 0})
            else:
                allInfections.append({'city':x['city'],'researchCenter':False,'blue':0,'black':0,'purple':0,'red':0,'yellow':0})
        return allInfections

    def get_infection(self, user, roomId):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        # return currentGame.mapInfection

        new_list = []
        for x in currentGame.mapInfection:
            mySum = x['blue']+x['black']+x['red']+x['yellow']+x['purple']
            new_list.append([x['city'], mySum, x['blue'], x['black'], x['red'], x['yellow'], x['purple']])
        return new_list

    def get_infection_city(self, user, roomId, city):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        for x in currentGame.mapInfection:
            if x["city"] == city:
                return x

    def increment_infection(self, user, roomId, city, color, order):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        new_list=[]
        for x in order.split(","):
            for y in currentGame.mapInfection:
                if x == y["city"] and x == city:
                    infectedCity =  y
                    infectedCity[color] = infectedCity[color] + 1
                    new_list.append(infectedCity)
                    break
                elif x == y["city"]:
                    new_list.append(y)
                    break
        currentGame.mapInfection = new_list
        currentGame.save()

        if color == "blue": currentGame.blueTokens = currentGame.blueTokens-1
        elif color == "black": currentGame.blackTokens = currentGame.blackTokens-1
        elif color == "red": currentGame.redTokens = currentGame.redTokens-1
        elif color == "yellow": currentGame.yellowTokens = currentGame.yellowTokens-1
        elif color == "purple": currentGame.purpleTokens = currentGame.purpleTokens-1
        currentGame.save()

    def decrement_infection(self, user, roomId, city, color, order):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        new_list = []
        for x in order.split(","):
            for y in currentGame.mapInfection:
                if x == y["city"] and x == city:
                    infectedCity = y
                    infectedCity[color] = infectedCity[color] - 1
                    new_list.append(infectedCity)
                    break
                elif x == y["city"]:
                    new_list.append(y)
                    break
        currentGame.mapInfection = new_list
        currentGame.save()

        if color == "blue": currentGame.blueTokens = currentGame.blueTokens+1
        elif color == "black": currentGame.blackTokens = currentGame.blackTokens+1
        elif color == "red": currentGame.redTokens = currentGame.redTokens+1
        elif color == "yellow": currentGame.yellowTokens = currentGame.yellowTokens+1
        elif color == "purple": currentGame.purpleTokens = currentGame.purpleTokens+1
        currentGame.save()



    def get_location(self,roomId):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.filter(roomId=roomObj).values()
        new_list = []
        for x in p:
            new_list.append({'user': x["playerName"], 'currentLocation': x["currentLocation"]})
        return new_list


    def toggle_research(self, roomId, city):
        roomObj = Room.objects.get(roomId=roomId)
        currentGame = Game.objects.get(roomId=roomObj)
        new_list = []
        for x in currentGame.mapInfection:
            if city == x["city"]:
                val = x["researchCenter"]
                if val == True:
                    val = False
                else:
                    val = True
                x["researchCenter"] = val
                new_list.append(x)
            else:
                new_list.append(x)
        currentGame.mapInfection = new_list
        currentGame.save()


    def set_location(self, roomId, user, city):
        roomObj = Room.objects.get(roomId=roomId)
        p = Player.objects.get(roomId=roomObj, playerName=user)
        p.currentLocation = city
        p.save()









