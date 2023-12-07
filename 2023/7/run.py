import collections

card_rank = "23456789TJQKA"


def get_sort_key(hand):
    key = 0
    for i, card in enumerate(hand[::-1]):
        card_key = card_rank.index(card)
        key += card_key * (100 ** (i))
    return key


hands = [[] for _ in range(7)]
with open("input.txt") as file:
    for line in file:
        hand, raw_bid = line.strip().split()
        bid = int(raw_bid)
        hand_counter = collections.Counter(hand)
        sort_key = get_sort_key(hand)

        if hand_counter.most_common()[0][1] == 5:
            hands[0].append((hand, bid, sort_key))

        elif hand_counter.most_common()[0][1] == 4:
            hands[1].append((hand, bid, sort_key))

        elif hand_counter.most_common()[0][1] == 3 and hand_counter.most_common()[1][1] == 2:
            hands[2].append((hand, bid, sort_key))

        elif hand_counter.most_common()[0][1] == 3:
            hands[3].append((hand, bid, sort_key))

        elif hand_counter.most_common()[0][1] == 2 and hand_counter.most_common()[1][1] == 2:
            hands[4].append((hand, bid, sort_key))

        elif hand_counter.most_common()[0][1] == 2:
            hands[5].append((hand, bid, sort_key))
        else:
            hands[6].append((hand, bid, sort_key))

final_hands = []
for hands_by_rank in hands[::-1]:
    hands_by_rank.sort(key=lambda x : x[2])
    final_hands.extend(hands_by_rank)

winnings = 0
for i in range(len(final_hands)):
    winnings += final_hands[i][1] * (i+1)
print(winnings)