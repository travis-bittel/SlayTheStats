from typing import Optional, Set

BOSS_RELIC_FLOORS = {
    0: 17,
    1: 34,
    2: 51
}


class RelicData:
    def __init__(self, name: str, floor_obtained: int, floor_lost: Optional[int]):
        self.name: str = name
        self.floor_obtained: int = floor_obtained
        self.floor_lost: Optional[int] = floor_lost


def all_relics(run_json_data) -> Set[RelicData]:
    relic_data: Set[RelicData] = set()

    relic_names = all_relic_names(run_json_data)
    for relic_name in relic_names:
        floor_obtained = 0
        for relic_obtained in run_json_data['relics_obtained']:
            if relic_obtained['key'] == relic_name:
                floor_obtained = relic_obtained['floor']
        for i, boss_relic_choice in enumerate(run_json_data['boss_relics']):
            if "picked" in boss_relic_choice and boss_relic_choice['picked'] == relic_name:
                floor_obtained = BOSS_RELIC_FLOORS[i]
        for event_choice in run_json_data['event_choices']:
            if "relics_obtained" in event_choice and event_choice['relics_obtained'][0] == relic_name:
                floor_obtained = event_choice['floor']

        floor_lost = None
        for event_choice in run_json_data['event_choices']:
            if "relics_lost" in event_choice and event_choice['relics_lost'][0] == relic_name:
                floor_lost = event_choice['floor']

        relic_data.add(RelicData(relic_name, floor_obtained, floor_lost))

    return relic_data


def all_relic_names(run_json_data) -> {str}:
    relic_names = set()

    # Add all relics held at end of run
    for relic in run_json_data['relics']:
        relic_names.add(relic)
    # Add all relics lost during the run
    for event_choice in run_json_data['event_choices']:
        if 'relics_lost' in event_choice:
            # Even though this field is named with an s, it only ever contains 1 relic
            relic_names.add(event_choice['relics_lost'][0])

    return relic_names


def relic_was_owned_at_floor(floor: int, relic_data: RelicData):
    return (floor >= relic_data.floor_obtained and
            (not relic_data.floor_lost or floor < relic_data.floor_lost))
