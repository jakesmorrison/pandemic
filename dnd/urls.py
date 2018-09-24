from django.conf.urls import url
from . import views

app_name = 'dnd'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^combat$', views.combat, name='combat'),
    url(r'^spells', views.spells, name='spells'),
    url(r'^get_spells', views.get_spells, name='get_spells'),
    url(r'^monsters', views.monsters, name='monsters'),
    url(r'^get_monsters', views.get_monsters, name='get_monsters'),
]
