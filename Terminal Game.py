import random

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
card_scores = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_count = [4] * len(cards)
card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.score = card_scores[cards.index(value)]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in card_suits:
            for value in cards:
                self.cards.append(Card(suit, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def add_card(self, card):
        self.cards.append(card)
        self.score += card.score

        # Adjust the score for Aces
        if self.score > 21:
            for c in self.cards:
                if c.value == "Ace" and c.score == 11:
                    c.score = 1
                    self.score -= 10
                    break

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def show_hand(self, reveal=False):
        if reveal:
            print("Dealer's Hand:")
            for card in self.hand.cards:
                print(f" {card.value} of {card.suit}")
            print(f"Score: {self.hand.score}")
        else:
            print("Dealer's Hand:")
            print(f" {self.hand.cards[0].value} of {self.hand.cards[0].suit}")
            print(" <card hidden>")

    def play(self, deck):
        self.show_hand(reveal=True)
        while self.hand.score < 17:
            print("Dealer hits!")
            self.hand.add_card(deck.deal())
            print(f"Dealer's new card: {self.hand.cards[-1].value} of {self.hand.cards[-1].suit}")
            print(f"New score: {self.hand.score}")
        if self.hand.score > 21:
            print("Dealer busts!")

class Player:
    def __init__(self):
        self.hand = Hand()

    def show_hand(self):
        print("Your Hand:")
        for card in self.hand.cards:
            print(f" {card.value} of {card.suit}")
        print(f"Score: {self.hand.score}")

    def hit(self, deck):
        self.hand.add_card(deck.deal())
        print(f"Your new card: {self.hand.cards[-1].value} of {self.hand.cards[-1].suit}")
        print(f"New score: {self.hand.score}")
        if self.hand.score > 21:
            print("You bust!")

    def play(self, deck):
        while True:
            self.show_hand()
            action = input("Do you want to hit or stand? ")
            if action == "hit":
                self.hit(deck)
                if self.hand.score > 21:
                    break
            elif action == "stand":
                break
print("Welcome to Blackjack!")
play = input("to play Press Y: ")
if play.lower() == "y":
    player = Player()
    dealer = Dealer()
    deck = Deck()

    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())
    player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())

    dealer.show_hand()

    player.play(deck)

    if player.hand.score <= 21:
        dealer.play(deck)

    if player.hand.score > 21:
        print("You lose!")
    elif dealer.hand.score > 21:
        print("You win!")
    elif player.hand.score > dealer.hand.score:
        print("You win!")
    elif player.hand.score < dealer.hand.score:
        print("You lose!")
    else:
        print("It's a tie!")
else:
    print("bye")