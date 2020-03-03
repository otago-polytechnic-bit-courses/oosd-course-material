from random import shuffle

card_values = {"2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "10": 10,
               "J": 10,
               "Q": 10,
               "K": 10,
               "A": 11,
               }

class Deck():
    def __init__(self):
        self.cards = []
        for _ in range(1, 4):
            self.cards.extend(card_values.keys())

        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player():
    def __init__(self):
        self.cards = []

    def print_cards(self):
        return ", ".join(self.cards)

    def score(self):
        score = sum([card_values[c] for c in self.cards])
        return score if score <= 21 else -1  # -1 means you busted

    def draw(self, deck):
        if input("Do you want a card?") in ("Y", 'y'):
            self.cards.append(deck.draw())
            return True


class HousePlayer(Player):
    def __init__(self, target_score):
        super().__init__()
        self.target_score = target_score
        
    def draw(self, deck):
        while self.score() < self.target_score and self.score() >= 0:
            self.cards.append(deck.draw())
            return True
            
        
if __name__ == "__main__":
    player = Player()
    deck = Deck()
    while player.draw(deck):
        print("You have %s (=%d)." % (player.print_cards(), player.score()))

    house = HousePlayer(player.score())
    while house.draw(deck):
        print("House has %s (=%d)." % (house.print_cards(), house.score()))

    print("You won!" if player.score() > house.score() else "You lost!")
