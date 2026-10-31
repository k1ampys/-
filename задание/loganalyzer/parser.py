from dataclasses import dataclass
from datetime import datetime, timezone
import re

LEVELS = {"TRACE", "DEBUG", "INFO", "WARN", "ERROR"}
_TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

@dataclass(frozen=True)
class Record:
    ts: datetime
    level: str
    source: str
    event_code: str
    message: str

@dataclass(frozen=True)
class ParseError:
    line_no: int
    reason: str
    raw: str

def parse_timestamp(value: str) -> datetime:
    if not _TS_RE.match(value):
        raise ValueError(f"timestamp is not ISO 8601 UTC with 'Z': {value!r}")
    dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    return dt.replace(tzinfo=timezone.utc)

def parse_line(line_no: int, raw: str) -> Record | ParseError:
    line = raw.rstrip("\n")
    if not line.strip():
        return ParseError(line_no, "empty line", raw)
    parts = line.split("|")
    if len(parts) != 5:
        return ParseError(line_no, f"expected 5 fields, got {len(parts)}", raw)
    ts_s, level_s, source_s, code_s, msg_s = (p.strip() for p in parts)
    if not ts_s:
        return ParseError(line_no, "empty timestamp", raw)
    try:
        ts = parse_timestamp(ts_s)
    except ValueError as e:
        return ParseError(line_no, str(e), raw)
    if not level_s:
        return ParseError(line_no, "empty level", raw)
    if level_s not in LEVELS:
        return ParseError(line_no, f"unsupported level: {level_s!r}", raw)
    if not source_s:
        return ParseError(line_no, "empty source", raw)
    if not code_s:
        return ParseError(line_no, "empty event code", raw)
    return Record(ts=ts, level=level_s, source=source_s, event_code=code_s, message=msg_s)
