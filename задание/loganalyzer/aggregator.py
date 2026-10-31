from collections import Counter
from .parser import Record

class Aggregator:
    def __init__(self, top_n: int = 5):
        self.top_n = top_n
        self.total_lines = 0
        self.valid_lines = 0
        self.invalid_lines = 0
        self.matched = 0
        self.by_level = Counter()
        self.by_source = Counter()
        self.by_error_code = Counter()

    def add_valid(self, rec: Record, matched: bool) -> None:
        self.valid_lines += 1
        if matched:
            self.matched += 1
            self.by_level[rec.level] += 1
            self.by_source[rec.source] += 1
            if rec.level == "ERROR":
                self.by_error_code[rec.event_code] += 1

    def add_invalid(self) -> None:
        self.invalid_lines += 1

    def top_errors(self) -> list[tuple[str, int]]:
        items = sorted(self.by_error_code.items(), key=lambda kv: (-kv[1], kv[0]))
        return items[: self.top_n]

    def as_dict(self) -> dict:
        return {
            "total_lines": self.total_lines,
            "valid_lines": self.valid_lines,
            "invalid_lines": self.invalid_lines,
            "matched_events": self.matched,
            "by_level": dict(sorted(self.by_level.items())),
            "by_source": dict(sorted(self.by_source.items())),
            "top_error_codes": [{"code": c, "count": n} for c, n in self.top_errors()]
        }
