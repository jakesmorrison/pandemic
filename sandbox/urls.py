from django.conf.urls import url
from . import views

app_name = 'sandbox'
urlpatterns = [
    url(r'micron_slider_test/', views.micron_slider_test, name='micron_slider_test'),
    url(r'new_demo_front_end/', views.new_demo_front_end, name='new_demo_front_end'),
    url(r'get_data/', views.get_data, name='get_data'),
    url(r'gary_spelling/', views.gary_spelling, name='gary_spelling'),
    url(r'career_day/', views.career_day, name='career_day'),
]