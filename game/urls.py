from django.conf.urls import url
from . import views

app_name = "game"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'log/', views.log, name='log'),
    url(r'signup/', views.signup, name='signup'),
    url(r'lobby/', views.lobby, name='lobby'),
    url(r'gameboard/', views.gameboard, name='gameboard'),
    url(r'dealcards/', views.dealcards, name='dealcards'),
    url(r'discardaction/', views.discardaction, name='discardaction'),
    url(r'getnewcard/', views.getnewcard, name='getnewcard'),
    url(r'infectionplaytop/', views.infectionplaytop, name='infectionplaytop'),
    url(r'infectionplaybottom/', views.infectionplaybottom, name='infectionplaybottom'),
    url(r'incrementcolor/', views.incrementcolor, name='incrementcolor'),
    url(r'decrementcolor/', views.decrementcolor, name='decrementcolor'),
    url(r'incrementother/', views.incrementother, name='incrementother'),
    url(r'decrementother/', views.decrementother, name='decrementother'),
    url(r'changecure/', views.changecure, name='changecure'),
    url(r'reshuffleinfectiondeck/', views.reshuffleinfectiondeck, name='reshuffleinfectiondeck'),
    url(r'removerole/', views.removerole, name='removerole'),
    url(r'savenotes/', views.savenotes, name='savenotes'),
    url(r'pickupdiscard/', views.pickupdiscard, name='pickupdiscard'),
    url(r'getinfectionmap/', views.getinfectionmap, name='getinfectionmap'),
    url(r'incrementinfection/', views.incrementinfection, name='incrementinfection'),
    url(r'decrementinfection/', views.decrementinfection, name='decrementinfection'),
    url(r'toggleresearch/', views.toggleresearch, name='toggleresearch'),
    url(r'setlocation/', views.setlocation, name='setlocation'),
    url(r'getplayercards/', views.getplayercards, name='getplayercards'),

]
