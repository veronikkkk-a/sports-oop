from dataclasses import dataclass, field
from sports_oop.value_objects import ScoreValue

@dataclass
class Sport:
    id: int
    name: str
    category: str

@dataclass
class Athlete:
    id: int
    full_name: str
    sport: Sport
    _rating: int = field(default=0, repr=False)

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, value: int) -> None:
        if value < 0:
            raise ValueError("Rating cannot be negative")
        self._rating = value

    def __str__(self) -> str:
        return f"{self.full_name} [{self.sport.name}]"

@dataclass
class Competition:
    id: int
    title: str
    location: str

@dataclass
class Result:
    id: int
    athlete: Athlete
    competition: Competition
    score: ScoreValue

    def __repr__(self) -> str:
        return f"Result(athlete={self.athlete.full_name!r}, score={self.score!r})"

class RankingTable:
    def __init__(self) -> None:
        self._items: list[Result] = []

    def add(self, result: Result) -> None:
        self._items.append(result)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __contains__(self, result_id: int) -> bool:
        return any(item.id == result_id for item in self._items)