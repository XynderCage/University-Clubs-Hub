from typing import Protocol, Sequence
from dataclasses import dataclass

@dataclass(frozen=True)
class ClubSummary:
    id: int
    name: str
    category: str
    description: str
    activities: str
    contact_name: str
    contact_email: str

class ClubRepository(Protocol):
    def search_verified(self, query: str = "", category: str = "") -> Sequence[ClubSummary]:
        """Return only verified clubs matching public search criteria."""
    def get_verified_by_id(self, club_id: int) -> ClubSummary | None:
        """Return a verified club or None; never expose unverified records."""
