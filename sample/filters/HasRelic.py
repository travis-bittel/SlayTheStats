from sample.filters.FloorFilter import FloorFilter
from sample.filters.RunFilter import RunFilter
import sample.run_data.relics as relics

class HasRelic(RunFilter, FloorFilter):
    def __init__(self, relic_name):
        self.relic_name = relic_name

    def matching_floors(self, floors: [int], run_data: dict) -> [int]:
        relics_in_run = relics.all_relics(run_data)

        relics_matching_filter_name = [relic_data for relic_data in relics_in_run if relic_data.name == self.relic_name]
        if not relics_matching_filter_name:
            return []
        relic_to_filter_by = relics_matching_filter_name[0]

        return [floor for floor in floors if relics.relic_was_owned_at_floor(floor, relic_to_filter_by)]

    def matching_runs(self, runs: [dict]) -> [dict]:
        return [run for run in runs if self.relic_name in [relic.name for relic in relics.all_relics(run)]]

