from sample.filters.FloorFilter import FloorFilter
from sample.filters.RunFilter import RunFilter


class Attribute:
    """Given a set of runs and filters to apply, returns the data points for the attribute."""
    def get(self, runs: [dict], run_filters: [RunFilter] = None, floor_filters: [FloorFilter] = None):
        pass
