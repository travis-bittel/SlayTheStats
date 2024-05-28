from sample.attributes.Attribute import Attribute
from sample.filters.FloorFilter import FloorFilter
from sample.filters.RunFilter import RunFilter
from sample.run_data.CardChoice import CardChoice
import sample.run_data.card_choices as card_choices
import sample.run_data.floors as floors


class CardElo(Attribute):
    def get(self, runs: [dict], run_filters: [RunFilter] = None, floor_filters: [FloorFilter] = None) -> dict:
        card_choices_to_count = []
        if run_filters is not None:
            for run_filter in run_filters:
                runs = run_filter.matching_runs(runs)
        for run in runs:
            floors_to_count = floors.all_floors_reached(run)
            if floor_filters is not None:
                for floor_filter in floor_filters:
                    floors_to_count = floor_filter.matching_floors(floors_to_count, run)
            card_choices_to_count.extend(card_choices.get_card_choices_for_run(run, floors_to_count))

        return calculate_card_elo_ratings_for_set(card_choices_to_count)


def calculate_card_elo_ratings_for_set(choices: [CardChoice], starting_ratings: dict = None):
    if starting_ratings is None:
        card_elo_ratings = {}
    else:
        card_elo_ratings = starting_ratings

    for card_choice in choices:
        for card in card_choice.all_cards():
            if card not in card_elo_ratings:
                card_elo_ratings[card] = 1000

        rating_adjustments = elo_rating_adjustments_for_card_choice(card_elo_ratings, card_choice)
        for card in card_choice.all_cards():
            card_elo_ratings[card] += rating_adjustments[card]

    return card_elo_ratings


def elo_rating_adjustments_for_card_choice(card_elo_ratings: [float], card_choice: CardChoice):
    total_rating_adjustments = {}

    for card in card_choice.all_cards():
        total_rating_adjustments[card] = 0

    for skipped_card in card_choice.cards_skipped:
        rating_adjustments = elo_rating_adjustments(card_elo_ratings[card_choice.card_picked],
                                                    card_elo_ratings[skipped_card])
        total_rating_adjustments[card_choice.card_picked] += rating_adjustments[0]
        total_rating_adjustments[skipped_card] += rating_adjustments[1]

    return total_rating_adjustments


def elo_rating_adjustments(previous_winner_rating, previous_loser_rating):
    return [32 * (1 - probability_of_winning_as_decimal(previous_winner_rating, previous_loser_rating)),
            -32 * (probability_of_winning_as_decimal(previous_loser_rating, previous_winner_rating))]


def probability_of_winning_as_decimal(rating1, rating2):
    return 1 / (1 + 10 ** ((rating2 - rating1) / 400))
