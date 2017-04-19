from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Room, Game
from .management import methods
from .management import config as cfg
import json
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.

@login_required
def index(request):
    pd = methods.Pandemic()
    roomInfo = Room.objects.order_by("id").values()
    roomId = pd.generate_game_id(Room, "roomId")
    context = {
        "user":request.user.username,
        "roomInfo":roomInfo,
        "roomId": roomId,
    }
    return render(request,"game/lobby.html",context)

def log(request):
    username = request.POST['logged_user']
    password = request.POST['logged_password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        context = {}
        return render(request, "game/invalid_user.html", context)

def signup(request):
    username = request.POST['new_user']
    password = request.POST['new_password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    user = authenticate(username=username, password=password)
    login(request, user)
    return HttpResponseRedirect("/")

def lobby(request):
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return index(request)
    else:
        context = {}
        return render(request, "game/invalid_user.html", context)


def gameboard(request,rId):
    pd = methods.Pandemic()
    params = request.POST
    if "new" in params:
        pd.add_room(roomId = params["roomId"], createdBy = params["createdBy"],mutation = params["mutation"],
                    numberOfPandemicCards = params["numpandemiccards"],numberOfRoleCards = params["numrolecards"])
    mapData = pd.get_lat_long()

    connectionData = pd.connect_cities()

    context = {
        "roomId": params["roomId"],
        "blueTokens":cfg.Config.maxCubes,
        "blackTokens": cfg.Config.maxCubes,
        "redTokens": cfg.Config.maxCubes,
        "yellowTokens": cfg.Config.maxCubes,
        "purpleTokens": int(cfg.Config.maxCubes/2),
        "infectionRate":cfg.Config.infectionRate[0],
        "outbreaks": cfg.Config.outbreaks,
        "mapData": mapData,
        "connectionData":connectionData,
    }
    return render(request, "game/gameboard.html", context)

def getplayercards(request):
    params = request.GET
    pd = methods.Pandemic()
    context = {
        'cards':pd.getcards(roomId=params["roomId"],user=params["user"]),
        'roles': pd.getrolecards(roomId=params["roomId"], user=params["user"])
    }
    return JsonResponse(json.loads(json.dumps(context)))


def dealcards(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.deal_cards(users = json.loads(json.dumps(params["users"])),roomId = params["roomId"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def discardaction(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.discardaction(roomId=params["roomId"],user=params["user"],city=params["city"])
    context={}
    return JsonResponse(json.loads(json.dumps(context)))

def getnewcard(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.getnewcard(roomId=params["roomId"],user=params["user"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def infectionplaytop(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.infectionplaytop(roomId=params["roomId"],user=params["user"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))


def infectionplaybottom(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.infectionplaybottom(roomId=params["roomId"], user=params["user"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def incrementcolor(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.incrementcolor(roomId=params["roomId"], user=params["user"],color=params["color"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))


def decrementcolor(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.decrementcolor(roomId = params["roomId"], user = params["user"], color = params["color"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def incrementother(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.incrementother(roomId = params["roomId"], user = params["user"], indicator = params["indicator"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))


def decrementother(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.decrementother(roomId = params["roomId"], user = params["user"], indicator = params["indicator"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def changecure(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.changecure(roomId = params["roomId"], user = params["user"], cureName = params["cureName"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def reshuffleinfectiondeck(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.reshuffleinfectiondeck(roomId = params["roomId"], user = params["user"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def removerole(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.removerole(roomId = params["roomId"], user = params["user"],role = params["role"].replace("_"," "))
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def savenotes(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.savenotes(roomId = params["roomId"], user = params["user"], note=params["note"])
    context = {"notes":pd.getnotes(roomId=params["roomId"],user=params["user"])}
    return JsonResponse(json.loads(json.dumps(context)))

def pickupdiscard(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.pickupdiscard(roomId = params["roomId"], user = params["user"], city=params["city"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def getinfectionmap(request):
    params = request.GET
    pd = methods.Pandemic()
    cityInfo = pd.get_infection_city(roomId = params["roomId"], user = params["user"], city=params["city"])
    context = {
        'cityInfo': cityInfo}
    return JsonResponse(json.loads(json.dumps(context)))

def incrementinfection(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.increment_infection(roomId = params["roomId"], user = params["user"], city=params["city"], color=params["color"], order=params["order"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))


def decrementinfection(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.decrement_infection(roomId = params["roomId"], user = params["user"], city=params["city"], color=params["color"], order=params["order"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def toggleresearch(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.toggle_research(roomId = params["roomId"], city=params["city"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def setlocation(request):
    params = request.GET
    pd = methods.Pandemic()
    pd.set_location(roomId = params["roomId"], user = params["user"], city=params["city"])
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))



