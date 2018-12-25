from django.contrib import admin
from .models import Room, Game, Player, CityCards, SpecialEventCards, \
    EmergencyEventCards, CityCards, EpidemicCards, MutationCards, InfectionCards, RolesCard

# Register your models here.

admin.site.register(
    CityCards,
    list_display=["city", "country", "population", "color", "type", "connectionCities", "lat", "long"],
    list_display_links=["city", "country", "population", "color", "type", "connectionCities", "lat", "long"],
)

admin.site.register(
    SpecialEventCards,
    list_display=["name", "rules", "action", "type"],
    list_display_links=["name", "rules", "action", "type"],
)

admin.site.register(
    EmergencyEventCards,
    list_display=["name", "rules", "action", "type"],
    list_display_links=["name", "rules", "action", "type"],
)

admin.site.register(
    EpidemicCards,
    list_display=["name", "description", "type"],
    list_display_links=["name", "description", "type"],
)

admin.site.register(
    MutationCards,
    list_display=["name", "rules", "action", "type"],
    list_display_links=["name", "rules", "action", "type"],
)

admin.site.register(
    InfectionCards,
    list_display=["city", "country", "color", "type"],
    list_display_links=["city", "country", "color", "type"],
)

admin.site.register(
    RolesCard,
    list_display=["name", "description", "color", "type"],
    list_display_links=["name", "description", "color", "type"],
)


admin.site.register(
    Room,
    list_display=["roomId", "createdBy", "numberOfPandemicCards", "numberOfRoleCards", "mutation"],
    list_display_links=["roomId", "createdBy", "numberOfPandemicCards", "numberOfRoleCards", "mutation"],
)

admin.site.register(
    Game,
    list_display=["gameId", "roomId", "gameStarted", "users", "infectionCards","infectionDiscards", "actionCards","actionDiscards",
                  "rollCards","blueTokens", "blackTokens","redTokens","yellowTokens","purpleTokens","infectionRate","outbreaks",
                  "blueCure","blackCure","redCure","yellowCure","purpleCure", "mapInfection"],
    list_display_links=["gameId", "roomId", "gameStarted", "users", "infectionCards","infectionDiscards", "actionCards","actionDiscards",
                  "rollCards","blueTokens", "blackTokens","redTokens","yellowTokens","purpleTokens","infectionRate","outbreaks",
                  "blueCure","blackCure","redCure","yellowCure","purpleCure", "mapInfection"],
)

admin.site.register(
    Player,
    list_display=["roomId", "playerId", "playerName", "playerCards", "rollCards", "color","currentLocation"],
    list_display_links=["roomId", "playerId", "playerName", "playerCards", "rollCards", "color","currentLocation"],
)


