from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("query/", views.query, name="query"),
    path("query/attributes", views.query_attributes, name="query_attributes"),
    path("query/characters", views.query_characters, name="query_characters"),
    path("query/filters", views.query_filters, name="query_filters"),
    path("query/execute", views.execute_query, name="execute_query"),
    path("players/", views.players, name="players"),
    path("players/<player_id>/", views.player, name="player"),
    path("players/<player_id>/runs/", views.runs, name="player_runs"),
]
