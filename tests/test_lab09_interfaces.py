import unittest

from src.club_service import ClubService
from src.interfaces_or_ports.club_repository import ClubSummary


class FakeClubRepository:
    def __init__(self):
        self.last_search = None
        self.club = ClubSummary(
            id=1,
            name="Robotics Club",
            category="Technology",
            description="Build and explore robots.",
            activities="Workshops",
            contact_name="Demo Contact",
            contact_email="robotics@example.edu",
        )

    def search_verified(self, query="", category=""):
        self.last_search = (query, category)
        return [self.club]

    def get_verified_by_id(self, club_id):
        return self.club if club_id == 1 else None


class Lab09InterfaceTests(unittest.TestCase):
    def setUp(self):
        self.repository = FakeClubRepository()
        self.service = ClubService(self.repository)

    def test_search_uses_repository_and_trims_input(self):
        results = self.service.search("  robot  ", "  Technology  ")

        self.assertEqual(
            self.repository.last_search, ("robot", "Technology")
        )
        self.assertEqual(results, [self.repository.club])

    def test_invalid_search_does_not_reach_repository(self):
        with self.assertRaises(ValueError):
            self.service.search("x" * 101)

        self.assertIsNone(self.repository.last_search)

    def test_details_use_repository(self):
        self.assertEqual(
            self.service.get_details(1), self.repository.club
        )
        self.assertIsNone(self.service.get_details(999))


if __name__ == "__main__":
    unittest.main()