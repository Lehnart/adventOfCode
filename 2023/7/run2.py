import collections
import itertools

card_rank = "J23456789TQKA"


def get_hand_rank(hand):
    J_indices = [i for i in range(len(hand)) if hand[i] == "J"]
    if J_indices:
        min_rank = 6
        products = itertools.product( card_rank[1:], repeat=len(J_indices))
        for product in products:
            current_hand = ""
            current_j_index = 0
            for character_index in range(5):
                if character_index in J_indices:
                    current_hand += product[current_j_index]
                    current_j_index += 1
                else:
                    current_hand += hand[character_index]
            rank = get_hand_rank(current_hand)
            if rank < min_rank:
                min_rank = rank
        return min_rank

    hand_counter = collections.Counter(hand)
    if hand_counter.most_common()[0][1] == 5:
        return 0

    elif hand_counter.most_common()[0][1] == 4:
        return 1

    elif hand_counter.most_common()[0][1] == 3 and hand_counter.most_common()[1][1] == 2:
        return 2

    elif hand_counter.most_common()[0][1] == 3:
        return 3

    elif hand_counter.most_common()[0][1] == 2 and hand_counter.most_common()[1][1] == 2:
        return 4

    elif hand_counter.most_common()[0][1] == 2:
        return 5

    else:
        return 6


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
        sort_key = get_sort_key(hand)

        hand_rank = get_hand_rank(hand)
        hands[hand_rank].append((hand, bid, sort_key))

final_hands = []
for hands_by_rank in hands[::-1]:
    hands_by_rank.sort(key=lambda x: x[2])
    final_hands.extend(hands_by_rank)

winnings = 0
for i in range(len(final_hands)):
    winnings += final_hands[i][1] * (i + 1)
print(winnings)
