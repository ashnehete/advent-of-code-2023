from collections import Counter
from enum import IntEnum
from functools import cmp_to_key, cache

with open('input.txt', 'r') as reader:
    data = reader.read().splitlines()

bids = {datum.split()[0]: int(datum.split()[1]) for datum in data}
hands = bids.keys()

print(hands)

CARD_MAP = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10
}


@cache
def get_card_value(card: str):
    if card.isdigit():
        return int(card)
    else:
        return CARD_MAP[card]


class Type(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def get_type(hand: str):
    hand_counts = Counter(hand).most_common()
    length = len(hand_counts)
    if length == 1:
        return Type.FIVE_OF_A_KIND
    elif length == 2:
        if hand_counts[0][1] == 4:
            return Type.FOUR_OF_A_KIND
        else:
            return Type.FULL_HOUSE
    elif length == 3:
        if hand_counts[0][1] == 3:
            return Type.THREE_OF_A_KIND
        else:
            return Type.TWO_PAIR
    elif length == 4:
        return Type.ONE_PAIR
    else:
        return Type.HIGH_CARD


for hand in hands:
    print(hand, get_type(hand).name)


def sort_fn(a, b):
    a_type = get_type(a)
    b_type = get_type(b)

    if a_type != b_type:
        return a_type - b_type
    else:
        for card_a, card_b in zip(a, b):
            if get_card_value(card_a) - get_card_value(card_b):
                return get_card_value(card_a) - get_card_value(card_b)
        return 0


sorted_hands = sorted(hands, key=cmp_to_key(sort_fn))
print(sorted_hands)

res = 0
for idx, hand in enumerate(sorted_hands):
    res += (idx + 1) * bids[hand]

print(f'res={res}')
