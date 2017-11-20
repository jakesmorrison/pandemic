from django.conf.urls import url
from . import views

app_name = 'creditcard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]