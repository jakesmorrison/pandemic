from django.conf.urls import url
from . import views

app_name = 'sandbox'
urlpatterns = [
    url(r'micron_slider_test/', views.micron_slider_test, name='micron_slider_test'),
    url(r'^change_led/$', views.change_led, name='change_led'),
    url(r'new_demo_front_end/', views.new_demo_front_end, name='new_demo_front_end'),
    url(r'get_data/', views.get_data, name='get_data'),
    url(r'gary_spelling/', views.gary_spelling, name='gary_spelling'),
    url(r'career_day/', views.career_day, name='career_day'),
    url(r'^linely_demo/$', views.linely_demo, name='linely_demo'),
    url(r'^get_data_linely_demo/$', views.get_data_linely_demo, name='get_data_linely_demo'),
    url(r'^speed_grade/$', views.speed_grade, name='speed_grade'),
    url(r'^vmworld/$', views.vmworld, name='vmworld'),
    url(r'^cnbu_dash/$', views.cnbu_dash, name='cnbu_dash'),
    url(r'^get_region_data/$', views.get_region_data, name='get_region_data'),
    # url(r'^dna/$', views.dna, name='dna'),
    # url(r'^post_led/$', views.post_led, name='post_led'),
]

