import itertools
from collections import Counter


HAND_TYPE = {
    "FIVE_OAK": 7,
    "FOUR_OAK": 6,
    "FULL_HOUSE": 5,
    "THREE_OAK": 4,
    "TWO_PAIR": 3,
    "ONE_PAIR": 2,
    "HIGH_CARD": 1,
}


CARD_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARD_RANK_J = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


class CamelCardsHand:
    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.bid = bid

    def __repr__(self) -> str:
        return self.cards

    def __lt__(self, other: object) -> bool:
        if other.hand_type() == self.hand_type():
            for i in range(len(self.cards)):
                if CARD_RANK.index(other.cards[i]) < CARD_RANK.index(self.cards[i]):
                    return True
                elif CARD_RANK.index(other.cards[i]) == CARD_RANK.index(self.cards[i]):
                    continue
                else:
                    return False
            return False
        else:
            return HAND_TYPE[other.hand_type()] < HAND_TYPE[self.hand_type()]

    def hand_type(self) -> str:
        card_counter = Counter(self.cards)
        counts = card_counter.most_common()
        n1 = counts[0][1]
        if n1 != 5:
            n2 = counts[1][1]
        else:
            n2 = 0
        if n1 == 5:
            return "FIVE_OAK"
        if n1 == 4:
            return "FOUR_OAK"
        if n1 == 3:
            if n2 == 2:
                return "FULL_HOUSE"
            else:
                return "THREE_OAK"
        if n1 == 2:
            if n2 == 2:
                return "TWO_PAIR"
            else:
                return "ONE_PAIR"
        else:
            return "HIGH_CARD"


class CamelCardsHandJoker:
    def __init__(self, cards: str, bid: int) -> None:
        self.bid = bid
        self.original_cards = cards[:]
        if "J" not in cards:
            self.cards = cards[:]
        else:
            card_counter = Counter(cards)
            candidate_hands = []
            permutations = itertools.product(CARD_RANK, repeat=card_counter["J"])
            for perm in permutations:
                temp_hand = cards[:]
                for card in perm:
                    temp_hand = temp_hand.replace("J", card, 1)
                candidate_hands.append(CamelCardsHand(temp_hand, 0))
            candidate_hands.sort()
            self.cards = candidate_hands[0].cards

    def __repr__(self) -> str:
        return f"{self.cards} (was: {self.original_cards})"

    def __lt__(self, other: object) -> bool:
        if other.hand_type() == self.hand_type():
            for i in range(len(self.cards)):
                if CARD_RANK_J.index(other.original_cards[i]) < CARD_RANK_J.index(
                    self.original_cards[i]
                ):
                    return True
                elif CARD_RANK_J.index(other.original_cards[i]) == CARD_RANK_J.index(
                    self.original_cards[i]
                ):
                    continue
                else:
                    return False
            return False
        else:
            return HAND_TYPE[other.hand_type()] < HAND_TYPE[self.hand_type()]

    def hand_type(self) -> str:
        card_counter = Counter(self.cards)
        counts = card_counter.most_common()
        n1 = counts[0][1]
        if n1 != 5:
            n2 = counts[1][1]
        else:
            n2 = 0
        if n1 == 5:
            return "FIVE_OAK"
        if n1 == 4:
            return "FOUR_OAK"
        if n1 == 3:
            if n2 == 2:
                return "FULL_HOUSE"
            else:
                return "THREE_OAK"
        if n1 == 2:
            if n2 == 2:
                return "TWO_PAIR"
            else:
                return "ONE_PAIR"
        else:
            return "HIGH_CARD"


def get_points(lines: str, handtype: object) -> int:
    hands_dealt = []
    lines = lines.split("\n")
    for line in lines:
        hands_dealt.append(handtype(line.split()[0], int(line.split()[1])))

    hands_dealt.sort()
    total = 0
    for index, hand in enumerate(hands_dealt):
        points = len(hands_dealt) - index
        total += points * hand.bid

    return total


def part_one(lines: str) -> int:
    return get_points(lines, CamelCardsHand)


def part_two(lines: str) -> int:
    return get_points(lines, CamelCardsHandJoker)


def day7():
    with open("d7/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day7()
