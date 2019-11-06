def judge_sum(non_a_sum, a_num):
    if a_num == 0:
        return non_a_sum, 0
    else:
        maxsum = non_a_sum + a_num
        need_eleven = 0
        # 尝试所有A能否取11
        for i in range(a_num + 1):
            temp = non_a_sum + i * 11 + (a_num - i)
            if temp > 21:
                break
            if temp > maxsum:
                maxsum = temp
                need_eleven = i
        return maxsum, need_eleven


class Card:
    def __init__(self, suit, num):
        self.suit = suit
        self.realnum = num
        if '2' <= num <= '9':
            self.num = int(num)
        elif num == '10' or num == 'J' or num == 'Q' or num == 'K':
            self.num = 10
        else:
            self.num = 0

    def __str__(self):
        return self.suit + self.realnum


class Hand:
    def __init__(self):
        self.card = []
        self.cardnum = 0
        self.non_a_sum = 0
        self.sum = 0
        self.a_num = 0
        self.ten_num = 0
        self.a = 0

    def addcard(self, card):
        self.card.append(card)
        self.cardnum += 1
        if card.num == 0:
            self.a_num += 1
        else:
            self.non_a_sum += card.num
        if card.num == 10:
            self.ten_num += 1
        self.sum, self.a = judge_sum(self.non_a_sum, self.a_num)


suittype = {'Spade': 1, 'Heart': 2, 'Diamond': 3, 'Club': 4}
realnum = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

mycard = Hand()
for i in range(2):
    suit, num = input().split()
    card = Card(suit, num)
    mycard.addcard(card)

while True:
    if mycard.sum < 17:
        print('Hit')
        suit, num = input().split()
        card = Card(suit, num)
        if card.num == 0:
            print(suit, '1 11')
        else:
            print(suit, str(card.num))
        mycard.addcard(card)
    else:
        print('Stand')
        mycard.card = sorted(mycard.card, key=lambda x: (realnum[x.realnum], suittype[x.suit]))
        for card in mycard.card:
            print(f'{card}', end=' ')
        print()
        if mycard.sum > 21:
            print('Bust')
        elif mycard.ten_num > 0 and mycard.a > 0:
            print('Blackjack')
        else:
            print(mycard.sum)
        break



