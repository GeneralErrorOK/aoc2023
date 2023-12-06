from typing import List


class ScratchCard:
    def __init__(
        self, card_number: int, winning_numbers: List[int], draw: List[int]
    ) -> None:
        self.id = card_number
        self._wins = winning_numbers
        self._draw = draw
        self._instances = 1

    def __repr__(self) -> str:
        return f"Card {self.id}: {self.get_cumulative_points()} pts, {self._instances} copies."

    @staticmethod
    def from_lottery_draw(lottery_draw_line: str):
        card_number = lottery_draw_line.split(":")[0].split()[1]
        winning_nrs = lottery_draw_line.split(":")[1].split("|")[0].split()
        draw_nrs = lottery_draw_line.split(":")[1].split("|")[1].split()
        return ScratchCard(card_number, winning_nrs, draw_nrs)

    def add_instance(self, count: int = 1):
        self._instances += count

    @property
    def instances(self):
        return self._instances

    def get_matching_numbers(self) -> List:
        return list(filter(lambda x: x in self._wins, self._draw))

    def number_of_matches(self) -> int:
        return len(self.get_matching_numbers())

    def get_cumulative_points(self) -> int:
        wins = self.get_matching_numbers()
        if len(wins) > 0:
            return 2 ** (len(wins) - 1)
        else:
            return 0


def day4():
    with open("d4/input1.txt", "r") as file:
        lines = file.read()
    lines = lines.split("\n")
    total_points = 0
    cards = []
    for line in lines:
        card = ScratchCard.from_lottery_draw(line)
        print(card)
        total_points += card.get_cumulative_points()
        cards.append(card)

    for index, card in enumerate(cards):
        card: ScratchCard
        cards: List[ScratchCard]
        points = card.number_of_matches()
        for offset in range(points):
            try:
                cards[index + offset + 1].add_instance(card.instances)
            except IndexError:
                pass

    amount_of_cards = 0
    for card in cards:
        print(card)
        amount_of_cards += card.instances

    print(f"Part one: total points = {total_points}")
    print(f"Part two: amount of cards = {amount_of_cards}")


if __name__ == "__main__":
    day4()
