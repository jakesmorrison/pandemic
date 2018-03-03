from django.conf.urls import url
from . import views

app_name = 'oscar'
urlpatterns = [
    url(r'^$', views.oscar, name='oscar'),
]
