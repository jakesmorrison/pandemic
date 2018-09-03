from django.conf.urls import url, include
from . import views

app_name = 'celebmatch'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^retrieve_image.*', views.retrieve_image, name='retrieve_image'),
]