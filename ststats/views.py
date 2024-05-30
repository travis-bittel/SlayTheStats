from django.shortcuts import render
from django.http import HttpResponse
import os

import ststats.query.runs.run_data_collectors as run_data_collectors
from ststats.query.attributes.CardElo import CardElo
from ststats.query.filters.HasRelic import HasRelic


# Create your views here.
def index(request):
    root_runs_folder = "C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs"
    runs = run_data_collectors.all_runs_in_folder(os.path.join(root_runs_folder, "IRONCLAD"))
    attribute = CardElo()

    data = attribute.get(runs, run_filters=[HasRelic('Burning Blood')])
    for key, value in sorted(((round(v), k) for k, v in data.items()), reverse=True):
        print([key, value])

    return HttpResponse(f"{data}")
