import sqlite3
from pathlib import Path
from src.interfaces_or_ports.club_repository import ClubSummary

class SQLiteClubRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self):
        conn = sqlite3.connect(self.db_path, timeout=5)
        conn.row_factory = sqlite3.Row
        return conn

    def _initialize(self):
        with self._connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS clubs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                activities TEXT NOT NULL DEFAULT '',
                contact_name TEXT NOT NULL,
                contact_email TEXT NOT NULL,
                verified INTEGER NOT NULL CHECK (verified IN (0,1))
            )""")
            db.execute("CREATE INDEX IF NOT EXISTS idx_clubs_verified_name ON clubs(verified, name)")
            count = db.execute("SELECT COUNT(*) FROM clubs").fetchone()[0]
            if count == 0:
                db.executemany("""INSERT INTO clubs
                    (name,category,description,activities,contact_name,contact_email,verified)
                    VALUES (?,?,?,?,?,?,?)""", [
                    ("Robotics Club","Technology","A community for robotics, automation and practical engineering.","Workshops; robot builds","A. Molefe","robotics@example.edu",1),
                    ("Debate Society","Academic","Develop public speaking, argumentation and critical thinking.","Weekly debates; tournaments","K. Dube","debate@example.edu",1),
                    ("Photography Club","Arts","Explore photography, composition and visual storytelling.","Photo walks; exhibitions","T. Ndlovu","photo@example.edu",1),
                    ("Unverified Astronomy Group","Science","Pending registration; not public.","Observation nights","Pending","pending@example.edu",0)
                ])

    @staticmethod
    def _to_model(row):
        return ClubSummary(row["id"], row["name"], row["category"], row["description"],
                           row["activities"], row["contact_name"], row["contact_email"])

    def search_verified(self, query="", category=""):
        sql = """SELECT * FROM clubs WHERE verified=1
                 AND (?='' OR name LIKE ? OR category LIKE ? OR description LIKE ? OR activities LIKE ?)
                 AND (?='' OR category = ?)
                 ORDER BY name"""
        term = f"%{query}%"
        with self._connect() as db:
            rows = db.execute(sql, (query, term, term, term, term, category, category)).fetchall()
        return [self._to_model(r) for r in rows]

    def get_verified_by_id(self, club_id):
        with self._connect() as db:
            row = db.execute("SELECT * FROM clubs WHERE id=? AND verified=1", (club_id,)).fetchone()
        return self._to_model(row) if row else None
