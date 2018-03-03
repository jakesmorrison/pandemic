from django.conf.urls import url
from . import views

app_name = 'oscar'
urlpatterns = [
    url(r'^$', views.oscar, name='oscar'),
    url(r'add_to_db/', views.add_to_db, name='add_to_db'),
]
