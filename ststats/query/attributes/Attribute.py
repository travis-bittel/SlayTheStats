from ststats.query.filters.FloorFilter import FloorFilter
from ststats.query.filters.RunFilter import RunFilter


class Attribute:
    """Given a set of runs and filters to apply, returns the data points for the attribute."""
    def get(self, runs: [dict], run_filters: [RunFilter] = None, floor_filters: [FloorFilter] = None):
        pass
