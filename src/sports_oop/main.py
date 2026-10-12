from sports_oop.models import Sport, Athlete, Competition, Result, RankingTable
from sports_oop.value_objects import ScoreValue
from sports_oop.repositories import InMemoryRepository
from sports_oop.services import SportsManagementService

class ConsoleNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[NOTIFICATION] To {recipient}: {message}")

def main() -> None:
    print("=== СИСТЕМА ОБЛІКУ СПОРТИВНИХ РЕЗУЛЬТАТІВ (LAB 4) ===")

    sport = Sport(id=1, name="Біг 100м", category="Професіонали")
    athlete = Athlete(id=1, full_name="Андрій Шевченко", sport=sport)
    athlete.rating = 1

    competition = Competition(id=101, title="Чемпіонат України", location="Львів")
    score = ScoreValue(points=10.50, unit="сек")

    print(f"Спортсмен: {athlete}, Рейтинг: {athlete.rating}")
    print(f"Оцінка (Value Object): {score}")

    result_repo = InMemoryRepository[Result]()
    notifier = ConsoleNotifier()
    service = SportsManagementService(result_repo=result_repo, notifier=notifier)

    registered_result = service.register_result(
        res_id=1,
        athlete=athlete,
        competition=competition,
        score=score
    )

    table = RankingTable()
    table.add(registered_result)

    print(f"Кількість результатів у таблиці (dunder __len__): {len(table)}")
    print(f"Чи є результат з ID 1 у таблиці (dunder __contains__): {1 in table}")
    print(f"Середній результат: {service.get_average_score():.2f} сек")

if __name__ == "__main__":
    main()