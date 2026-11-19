SUITS: list[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
    "Ace",
]


class Card:
    rank: str
    suit: str
    rank_index: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank_index == other.rank_index

    def __gt__(self, other: "Card") -> bool:
        return self.rank_index > other.rank_index

    def __lt__(self, other: "Card") -> bool:
        return self.rank_index < other.rank_index

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
