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
def ws_connect(message):
    message.reply_channel.send({'accept': True})
    # Add them to the right group
    Group("game").add(message.reply_channel)


# Unpacks the JSON in the received WebSocket frame and puts it onto a channel
# of its own with a few attributes extra so we can route it
# This doesn't need @channel_session_user as the next consumer will have that,
# and we preserve message.reply_channel (which that's based on)
def ws_receive(message):
    pd = methods.Pandemic()

    payload = json.loads(message['text'])
    print(payload)
    user = payload["user"]
    roomId = payload["roomId"]
    command = payload["command"]
    message= payload["message"]

    roomObj = Room.objects.get(roomId=roomId)
    if command == "join":
        userNames = pd.create_update_game(roomObj = roomObj, user = user)
        context = {
            "command":"add-users",
            "users": userNames
        }
        context = json.dumps(context)
        Group("game").send({
                "text": context,
            })
    elif command == "dealcards":
        context = {
            "command": "dealcards",
            "roomId": roomId,
        }
        context = json.dumps(context)
        Group("game").send({
                "text": context,
            })

    elif command == "getcards":
        context = {
            "command": "getcards",
            "roomId": roomId,
        }
        context = json.dumps(context)
        Group("game").send({
            "text": context,
        })

        # payload['reply_channel'] = message.content['reply_channel']
    # print(payload)
    # Channel("chat.receive").send(payload)


@channel_session_user
def ws_disconnect(message):
    Group("game").discard(message.reply_channel)
# for room_id in message.channel_session.get("rooms", set()):
    #     try:
    #         room = Room.objects.get(pk=room_id)
    #         # Removes us from the room's send group. If this doesn't get run,
    #         # we'll get removed once our first reply message expires.
    #         room.websocket_group.discard(message.reply_channel)
    #     except Room.DoesNotExist:
    #         pass



