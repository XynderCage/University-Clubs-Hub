import json, os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from src.sqlite_club_repository import SQLiteClubRepository
from src.club_service import ClubService

BASE = Path(__file__).resolve().parent.parent
DB_PATH = os.environ.get("CLUBS_DB", str(BASE / "data" / "clubs.db"))
service = ClubService(SQLiteClubRepository(DB_PATH))

class Handler(BaseHTTPRequestHandler):
    def _json(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/clubs":
            params = parse_qs(parsed.query)
            try:
                clubs = service.search(params.get("q", [""])[0], params.get("category", [""])[0])
                self._json(200, {"items": [c.__dict__ for c in clubs], "count": len(clubs)})
            except ValueError as exc:
                self._json(400, {"error": {"code": "INVALID_SEARCH", "message": str(exc)}})
            except Exception:
                self._json(503, {"error": {"code": "SERVICE_UNAVAILABLE", "message": "Club search is temporarily unavailable. Please retry."}})
            return
        if parsed.path.startswith("/api/clubs/"):
            try:
                club_id = int(parsed.path.rsplit("/", 1)[1])
                club = service.get_details(club_id)
                if club is None:
                    self._json(404, {"error": {"code": "CLUB_NOT_FOUND", "message": "Verified club not found."}})
                else:
                    self._json(200, club.__dict__)
            except ValueError:
                self._json(400, {"error": {"code": "INVALID_ID", "message": "Club identifier must be a positive integer."}})
            except Exception:
                self._json(503, {"error": {"code": "SERVICE_UNAVAILABLE", "message": "Club details are temporarily unavailable."}})
            return
        if parsed.path in ("/", "/index.html"):
            page = (BASE / "prototype" / "wireframes" / "search.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(page)))
            self.end_headers()
            self.wfile.write(page)
            return
        self._json(404, {"error": {"code": "NOT_FOUND", "message": "Resource not found."}})

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))

if __name__ == "__main__":
    print(f"University Clubs Hub demonstrator: http://127.0.0.1:8000 (DB: {DB_PATH})")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
