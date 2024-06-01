import datetime
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import os

import ststats.query.runs.run_data_collectors as run_data_collectors
from ststats.models import Run, Player
from ststats.query.attributes.CardElo import CardElo
from ststats.query.filters.HasRelic import HasRelic


def query(request):
    root_runs_folder = "C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs"
    runs_in_local_folder = run_data_collectors.all_runs_in_folder(os.path.join(root_runs_folder, "IRONCLAD"))
    attribute = CardElo()

    data = attribute.get(runs_in_local_folder, run_filters=[HasRelic('Burning Blood')])
    for key, value in sorted(((round(v), k) for k, v in data.items()), reverse=True):
        print([key, value])

    return HttpResponse(f"{data}")


@api_view(['GET', 'POST'])
def runs(request, player_id):
    if request.method == 'GET':
        player_runs = list(Run.objects.filter(player_id=player_id).values('data'))
        return JsonResponse({'runs': player_runs})
    if request.method == 'POST':
        run = Run.objects.create(player_id=player_id, upload_date=datetime.datetime.now(), data=json.loads(request.body))
        run.save()
        return HttpResponse(status=200)


@api_view(['POST'])
def players(request):
    if request.method == 'POST':
        run = Player.objects.create(account_creation_date=datetime.datetime.now(), display_name='Brussel')
        run.save()
        return HttpResponse(status=200)


def player(request, player_id):
    if request.method == 'GET':
        player_data = Player.objects.filter(id=player_id).values('display_name', 'account_creation_date')[0]
        print(player_data)
        return JsonResponse({'player': player_data}, safe=False)
