from django.conf.urls import url
from . import views

app_name = 'finance'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^investment_analyzer$', views.investment_analyzer, name='investment_analyzer'),
    url(r'^retirement_withdrawl', views.retirement_withdrawl, name='retirement_withdrawl'),
    url(r'^sankey', views.sankey, name='sankey'),
    url(r'^top', views.top, name='top'),
    url(r'^stock_tracker', views.stock_tracker, name='stock_tracker'),
]
