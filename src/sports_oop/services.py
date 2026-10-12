from sports_oop.models import Result, Athlete, Sport, Competition
from sports_oop.value_objects import ScoreValue
from sports_oop.repositories import InMemoryRepository
from sports_oop.protocols import NotifierProtocol

class SportsManagementService:
    def __init__(
        self,
        result_repo: InMemoryRepository[Result],
        notifier: NotifierProtocol
    ) -> None:
        self._result_repo = result_repo
        self._notifier = notifier

    def register_result(
        self, res_id: int, athlete: Athlete, competition: Competition, score: ScoreValue
    ) -> Result:
        result = Result(id=res_id, athlete=athlete, competition=competition, score=score)
        self._result_repo.add(result)
        self._notifier.send(athlete.full_name, f"New result registered: {score}")
        return result

    def get_average_score(self) -> float:
        results = self._result_repo.all()
        if not results:
            return 0.0
        return sum(r.score.points for r in results) / len(results)