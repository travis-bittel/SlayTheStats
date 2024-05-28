import sample.run_data.relics as relics
from sample.run_data.CardChoice import CardChoice


def get_card_choices_for_run(run_json: dict, floors: [int] = None):
    card_choices = []

    matching_relic_data = [relic_data for relic_data in relics.all_relics(run_json)
                           if relic_data.name == 'Singing Bowl']
    singing_bowl_data = None
    if matching_relic_data:
        singing_bowl_data = matching_relic_data[0]

    card_choices_json = run_json["card_choices"]
    for i, card_choice_json in enumerate(card_choices_json):
        include_singing_bowl = (singing_bowl_data and
                                relics.relic_was_owned_at_floor(card_choice_json['floor'], singing_bowl_data))
        card_choices.append(get_card_choice(card_choice_json, include_singing_bowl))

    if floors is not None:
        return [card_choice for card_choice in card_choices if card_choice.floor in floors]
    else:
        return card_choices


def get_card_choice(card_choice_json, include_singing_bowl=False):
    card_picked = card_choice_json["picked"]
    cards_skipped = card_choice_json["not_picked"]
    floor = card_choice_json['floor']

    if card_picked != "SKIP":
        cards_skipped += ["SKIP"]

    if include_singing_bowl and card_picked != "Singing Bowl":
        cards_skipped += ["Singing Bowl"]

    return CardChoice(card_picked, cards_skipped, floor)
