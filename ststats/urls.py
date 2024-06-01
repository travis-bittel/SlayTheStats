from django.urls import path

from . import views

urlpatterns = [
    path("query/", views.query, name=""),
    path("players/", views.players, name=""),
    path("players/<player_id>/", views.player, name=""),
    path("players/<player_id>/runs/", views.runs, name=""),
]
