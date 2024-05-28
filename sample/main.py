import os
import runs.run_data_collectors
from sample.attributes.CardElo import CardElo
from filters.HasRelic import HasRelic

root_runs_folder = "C:/Program Files (x86)/Steam/steamapps/common/SlayTheSpire/runs"

if __name__ == '__main__':
    runs = runs.run_data_collectors.all_runs_in_folder(os.path.join(root_runs_folder, "IRONCLAD"))
    attribute = CardElo()

    data = attribute.get(runs, run_filters=[HasRelic('Burning Blood'), HasRelic('Golden Idol')])
    for key, value in sorted(((round(v), k) for k, v in data.items()), reverse=True):
        print([key, value])

