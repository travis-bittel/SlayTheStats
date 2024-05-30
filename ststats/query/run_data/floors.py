def highest_floor_reached(run_json: dict) -> int:
    return run_json["floor_reached"]


def all_floors_reached(run_json: dict) -> [int]:
    return list(range(1, highest_floor_reached(run_json)))
