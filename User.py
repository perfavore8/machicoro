from Card import Card, CARD_TYPE, CARDS


class User:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.cards = cards
        self.money = 0

    def add_card(self, card: Card):
        self.cards.append(card)
    
    def do_move(self, roll: int, turn: bool):
        for card in self.cards:
            # print(roll)
            if roll in card.roll and turn is False and card.type == CARD_TYPE.get("Красная"):
                pass
            if roll in card.roll and turn is True and card.type == CARD_TYPE.get("Зеленая"):
                self.money += card.calculate_bonus(self.cards)
                print("%s карточка отработала!!!" % card.name, roll, turn)
            if roll in card.roll and card.type == CARD_TYPE.get("Синяя"):
                self.money += card.calculate_bonus(self.cards)
                print("%s карточка отработала!!!" % card.name)
            if roll in card.roll and turn is True and card.type == CARD_TYPE.get("Фиолетовая"):
                pass