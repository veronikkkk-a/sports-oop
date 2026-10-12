from typing import TypedDict

class AthletePayload(TypedDict):
    id: int
    full_name: str
    sport_name: str
    category: str