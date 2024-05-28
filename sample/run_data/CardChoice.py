class CardChoice:
    def __init__(self, card_picked: str, cards_skipped: [str], floor: int):
        self.card_picked = card_picked
        self.cards_skipped = cards_skipped
        self.floor = floor

    def all_cards(self) -> [str]:
        return [self.card_picked, *self.cards_skipped]
