from ststats.models import Player
from ststats.query.attributes import CardElo
from ststats.query.attributes.Attribute import Attribute
from ststats.query.filters import HasRelic

ATTRIBUTES = {
    'CardEloRatings': CardElo.CardElo
}

FILTERS = [
    {
        'name': 'HasRelic',
        'applicable_to': ['RUN', 'FLOOR'],
        'arguments': [
            {
                'name': 'relic_name',
                'type': 'STRING'
            }
        ]
    }
]

FILTERS_TO_CLASSES = {
    'HasRelic': HasRelic.HasRelic
}

CHARACTERS = [
    'IRONCLAD',
    'THE_SILENT',
    'DEFECT',
    'WATCHER'
]


class InvalidQueryException(Exception):
    pass


def query_from_json(json_data: dict) -> dict:
    return {
        'attribute': get_attribute(json_data),
        'player_ids': get_player_ids(json_data),
        'characters': get_characters(json_data),
        'run_filters': get_filters(json_data, 'run_filters'),
        'floor_filters': get_filters(json_data, 'floor_filters')
    }


def get_attribute(json_data: dict) -> Attribute:
    if 'attribute' not in json_data.keys():
        raise InvalidQueryException(f'Query is missing attribute')
    attribute_string = json_data['attribute']
    try:
        return ATTRIBUTES[attribute_string]
    except KeyError:
        raise InvalidQueryException(f'Attribute \'{attribute_string}\' does not exist')


def get_player_ids(json_data: dict) -> [int]:
    if 'player_ids' not in json_data.keys():
        return []
    player_ids = json_data['player_ids']
    for player_id in player_ids:
        if not Player.objects.filter(id=player_id).exists():
            raise InvalidQueryException(f'Player ID \'{player_id}\' does not exist')
    return player_ids


def get_characters(json_data: dict) -> [str]:
    if 'characters' not in json_data.keys():
        return []
    characters = json_data['characters']
    for character in characters:
        if character not in CHARACTERS:
            raise InvalidQueryException(f'Character \'{character}\' does not exist')
    return characters


def get_filters(json_data: dict, key: str) -> []:
    if key not in json_data.keys():
        return []
    filters = []
    for filter_json in json_data[key]:
        name, arguments = filter_json['name'], filter_json['arguments']
        if name not in FILTERS_TO_CLASSES:
            raise InvalidQueryException(f'Filter \'{name}\' does not exist')
        filter_object = FILTERS_TO_CLASSES[name](arguments)
        filters.append(filter_object)
    return filters
