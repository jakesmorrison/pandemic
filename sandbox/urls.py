from django.conf.urls import url
from . import views

app_name = 'sandbox'
urlpatterns = [
    url(r'micron_slider_test/', views.micron_slider_test, name='micron_slider_test'),
]