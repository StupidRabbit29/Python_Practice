#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import IntEnum


class Card:
    kSuit = IntEnum("SuitEum", ("Spade", "Heart", "Diamond", "Club"))
    kRank = IntEnum("RankEum", (list("A23456789") + ["10"] + list("JQK")))

    def __init__(self, suit, rank):
        self.suit = self.kSuit[suit]
        self.rank = self.kRank[rank]

    def show_card(self):
        print(
            self.suit.name, "1 11" if self.rank.value == 1 else self.rank.name
        )


class Hand:
    def __init__(self, initial):
        self.cards = []
        for i in range(len(initial)):
            self.add_card(initial[i])

    def add_card(self, cur_card):
        self.cards.append(Card(cur_card[0], cur_card[1]))

    def show_latest_card(self):
        self.cards[len(self.cards) - 1].show_card()

    def rank_sum(self):
        A_count, rank_sum, self.Big_A_count = 0, 0, 0
        for i in self.cards:
            rank_sum += i.rank.value if i.rank.value < 10 else 10
            A_count += 1 if i.rank.name == "A" else 0
        for i in range(A_count):
            if rank_sum + 10 <= 21:
                self.Big_A_count += 1
                rank_sum += 10
        return rank_sum

    def show_shuffled_cards(self):
        print(
            " ".join(
                [
                    i.suit.name + i.rank.name
                    for i in sorted(
                        self.cards, key=lambda x: (x.rank.value, x.suit.value)
                    )
                ]
            )
        )

    def check_black_jack(self):
        return len(self.cards) == 2 and (
            (self.cards[0].rank.name == "A" and self.cards[1].rank.value >= 10)
            or (
                self.cards[0].rank.value >= 10
                and self.cards[1].rank.name == "A"
            )
        )


class Player:
    def __init__(self, *args, **kwargs):
        pass

    def play(self):
        cur_hand = Hand((input().split(), input().split()))
        while cur_hand.rank_sum() < 17:
            print("Hit")
            cur_hand.add_card(input().split())
            cur_hand.show_latest_card()
        else:
            print("Stand")
        cur_hand.show_shuffled_cards()
        tmp_sum = cur_hand.rank_sum()
        if tmp_sum > 21:
            print("Bust")
        elif cur_hand.check_black_jack():
            print("Blackjack")
        else:
            print(tmp_sum)


# for k, v in product(
#     Card.kSuit.__members__.items(), Card.kRank.__members__.items()
# ):
#     print(k, v)

P1 = Player()
P1.play()
