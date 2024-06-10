import datetime
import json
from json import JSONDecodeError

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.decorators import api_view

from ststats.query.query import ATTRIBUTES, CHARACTERS, FILTERS, query_from_json, InvalidQueryException
from ststats.models import Run, Player


def query(request):
    return render(request, "query.html")


def query_attributes(request):
    return JsonResponse({'attributes': list(ATTRIBUTES.keys())})


def query_characters(request):
    return JsonResponse({'characters': CHARACTERS})


def query_filters(request):
    return JsonResponse({'filters': FILTERS})


def execute_query(request):
    try:
        data = json.load(request)
    except JSONDecodeError:
        # TODO: Pull this out to a function and figure out how we want to display errors in general
        return HttpResponseBadRequest('<h1>400 BAD REQUEST</h1>Query request is not valid JSON')

    try:
        query_to_run = query_from_json(data)
    except InvalidQueryException as err:
        return HttpResponseBadRequest(f'<h1>400 BAD REQUEST</h1>{err}')

    runs_json = [run.data for run in list(Run.objects.all())]
    return JsonResponse(query_to_run['attribute']().get(runs=runs_json, run_filters=query_to_run['run_filters'],
                                                        floor_filters=query_to_run['floor_filters']))


@api_view(['GET', 'POST'])
def runs(request, player_id):
    if request.method == 'GET':
        player_runs = list(Run.objects.filter(player_id=player_id).values('data'))
        return JsonResponse({'runs': player_runs})
    if request.method == 'POST':
        run = Run.objects.create(player_id=player_id, upload_date=datetime.datetime.now(),
                                 data=json.loads(request.body))
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
