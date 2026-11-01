from src.interfaces_or_ports.club_repository import ClubRepository, ClubSummary

class ClubService:
    """Application boundary for the public club discovery use case."""
    def __init__(self, repository: ClubRepository):
        self._repository = repository

    def search(self, query: str = "", category: str = "") -> list[ClubSummary]:
        query = (query or "").strip()
        category = (category or "").strip()
        if len(query) > 100 or len(category) > 60:
            raise ValueError("Search criteria are too long.")
        return list(self._repository.search_verified(query, category))

    def get_details(self, club_id: int) -> ClubSummary | None:
        if not isinstance(club_id, int) or club_id < 1:
            raise ValueError("A positive club identifier is required.")
        return self._repository.get_verified_by_id(club_id)
