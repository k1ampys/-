from dataclasses import dataclass
from datetime import datetime
from .parser import Record

@dataclass(frozen=True)
class Filters:
    from_ts: datetime | None = None
    to_ts: datetime | None = None
    level: str | None = None
    source: str | None = None

    def matches(self, rec: Record) -> bool:
        if self.from_ts is not None and rec.ts < self.from_ts: return False
        if self.to_ts is not None and rec.ts >= self.to_ts: return False
        if self.level is not None and rec.level != self.level: return False
        if self.source is not None and rec.source != self.source: return False
        return True
