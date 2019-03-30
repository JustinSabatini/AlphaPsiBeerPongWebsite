from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'leaguerules', views.leaguerules, name='leaguerules'),
    url(r'rules', views.rules, name='rules'),
    url(r'teamstandings', views.teamstandings, name='teamstandings'),
    url(r'playerstats', views.playerstats, name='playerstats'),
    url(r'roster', views.roster, name='roster'),
    url(r'games', views.games, name='games'),
    url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    ]
