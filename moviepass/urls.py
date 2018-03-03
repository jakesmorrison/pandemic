from django.conf.urls import url
from . import views

app_name = 'moviepass'
urlpatterns = [
    url(r'^$', views.moviepass, name='moviepass'),
    url(r'^oscar$', views.oscar, name='oscar'),
]
