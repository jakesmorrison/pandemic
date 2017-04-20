from channels.routing import route
from game.consumers import ws_connect, ws_receive, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect, path=r'^/gameboard/(?P<rId>[^/]+)/stream/$'),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect, path=r'^/gameboard/(?P<rId>[^/]+)/stream/$'),
]
