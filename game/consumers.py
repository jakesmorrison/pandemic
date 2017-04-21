'''
Tutorial found here https://channels.readthedocs.io/en/stable/getting-started.html
'''

from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
import json
from .models import Game, Room, Player
from .management import methods


# This decorator copies the user from the HTTP session (only available in
# websocket.connect or http.request messages) to the channel session (available
# in all consumers with the same reply_channel, so all three here)
@channel_session_user_from_http
def ws_connect(message,rId):
    message.reply_channel.send({'accept': True})
    Group("game"+str(rId)).add(message.reply_channel)


# Unpacks the JSON in the received WebSocket frame and puts it onto a channel
# of its own with a few attributes extra so we can route it
# This doesn't need @channel_session_user as the next consumer will have that,
# and we preserve message.reply_channel (which that's based on)
def ws_receive(message):
    payload = json.loads(message['text'])
    command = payload["command"]

    pd = methods.Pandemic()
    user = payload["user"]
    roomId = payload["roomId"]

    if command == "join": join_game(pd,user,roomId,command)
    elif command == "dealcards": update_all(pd,user,roomId,command)
    elif command == "updatetokens": update_tokens(pd,user,roomId,command)
    elif command == "updateactioncards": update_action_cards(pd,user,roomId,command)
    elif command == "updateinfectioncards": update_infection_cards(pd, user, roomId, command)
    elif command == "updatecures": update_cure(pd, user, roomId, command)
    elif command == "updateinfectionmap": update_infection_map(pd, user, roomId, command)
    elif command == "updatecurrentlocation": update_current_location(pd, user, roomId, command)

def join_game(pd,user,roomId,command):
    roomObj = Room.objects.get(roomId=roomId)
    gameStarted = False
    if Game.objects.filter(roomId=roomObj).exists():
        gameObj = Game.objects.get(roomId=roomObj)
        if gameObj.gameStarted == True:
            gameStarted = True

    if gameStarted == False:
        userNames = pd.create_update_game(roomObj=roomObj, user=user)
        context = {
            "command": command,
            "roomId": roomId,
            "users": userNames,
        }
        context = json.dumps(context)
        Group("game"+str(roomId)).send({
            "text": context,
        })
    else:
        update_all(pd,user,roomId,command)

def update_all(pd,user,roomId,command):
    context = {
        "command": "updateall",
        "user": user,
        "roomId": roomId,
        'tokens': pd.gettokens(user=user, roomId=roomId),
        'actionCards': pd.getactioncards(user=user, roomId=roomId),
        'actionDiscards':pd.getactiondiscards(user=user, roomId=roomId),
        'infectionCards': pd.getinfectioncards(roomId=roomId, user=user),
        'infectionDiscards': pd.getinfectiondiscards(roomId=roomId, user=user),
        'userLocation': pd.get_location(roomId=roomId),
        'infectionMap': pd.get_infection(roomId=roomId, user=user),
        'cures': pd.getcures(user = user, roomId = roomId),
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({
        "text": context,
    })


def update_tokens(pd,user,roomId,command):
    context ={
        'command': command,
        'tokens': pd.gettokens(user=user, roomId=roomId),
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({ "text": context})

def update_action_cards(pd,user,roomId,command):
    context ={
        'command': command,
        'actionCards': pd.getactioncards(user=user, roomId=roomId),
        'actionDiscards':pd.getactiondiscards(user=user, roomId=roomId),
        'playerCards': pd.getcards(user=user, roomId=roomId),
        'roles': pd.getrolecards(user=user, roomId=roomId)
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({ "text": context})

def update_infection_cards(pd,user,roomId,command):
    context ={
        'command': command,
        'infectionCards': pd.getinfectioncards(roomId=roomId, user=user),
        'infectionDiscards': pd.getinfectiondiscards(roomId=roomId, user=user),
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({ "text": context})


def update_cure(pd,user,roomId,command):
    context ={
        'command': command,
        'cures': pd.getcures(user = user, roomId = roomId)
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({ "text": context})

def update_infection_map(pd,user,roomId,command):
    context ={
        'command': command,
        'infectionMap': pd.get_infection(roomId=roomId, user=user),
        'tokens': pd.gettokens(user=user, roomId=roomId),
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({ "text": context})

def update_current_location(pd,user,roomId,command):
    context = {
        "command": command,
        'userLocation': pd.get_location(roomId=roomId),
    }
    context = json.dumps(context)
    Group("game"+str(roomId)).send({"text": context})

@channel_session_user
def ws_disconnect(message, rId):
    Group("game"+str(rId)).discard(message.reply_channel)

