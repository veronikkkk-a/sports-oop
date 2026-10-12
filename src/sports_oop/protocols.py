from typing import Protocol, runtime_checkable
from sports_oop.models import Result

@runtime_checkable
class RankingStrategy(Protocol):
    def calculate_rank(self, results: list[Result]) -> list[Result]:
        ...

@runtime_checkable
class NotifierProtocol(Protocol):
    def send(self, recipient: str, message: str) -> None:
        ...