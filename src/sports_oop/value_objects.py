from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ScoreValue:
    points: float
    unit: str = "pts"

    def __post_init__(self) -> None:
        if self.points < 0:
            raise ValueError("Score points cannot be negative")

    def __str__(self) -> str:
        return f"{self.points:.2f} {self.unit}"