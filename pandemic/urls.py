"""pandemic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^pandemic/', include('game.urls')),
    url(r'^finance/', include('finance.urls')),
    url(r'^softball/', include('softball.urls')),
    url(r'^resume/', include('resume.urls')),
    url(r'^map/', include('map.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^definitions/', include('definitions.urls')),
    url(r'^travel/', include('travel.urls')),
    url(r'^heartbeat/', include('heartbeat.urls')),
    url(r'^loveletter/', include('loveletter.urls')),
    url(r'^justpooped/', include('poo.urls')),
    url(r'^travelbuddies/', include('travelbuddies.urls')),
    url(r'^asiatrip/', include('asia.urls')),
    url(r'^customdesign/', include('customdesign.urls')),
    url(r'^workout/', include('workout.urls')),
    url(r'^creditcard/', include('creditcard.urls')),
    url(r'^moviepass/', include('moviepass.urls')),
    url(r'^sandbox/', include('sandbox.urls')),
    url(r'^oscar/', include('oscar.urls')),
    url(r'^dnd/', include('dnd.urls')),
    url(r'^celebmatch/', include('celebmatch.urls')),
    url(r'', include('homepage.urls')),
]
