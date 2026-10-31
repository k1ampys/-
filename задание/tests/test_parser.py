from datetime import datetime, timezone
from loganalyzer.parser import parse_line, Record, ParseError, parse_timestamp

def test_valid_line():
    r = parse_line(1, "2026-09-01T00:08:59Z | WARN | auth-api | AUTH_LOGIN_OK | User session created\n")
    assert isinstance(r, Record)
    assert r.level == "WARN" and r.source == "auth-api"

def test_bad_timestamp():
    assert isinstance(parse_line(1, "not-a-timestamp | ERROR | orders-api | X | msg"), ParseError)

def test_bad_level_and_empty_fields():
    assert isinstance(parse_line(1, "2026-09-01T00:00:00Z | NOTICE | g | E | m"), ParseError)
    assert isinstance(parse_line(1, "2026-09-01T00:00:00Z |  | g | E | m"), ParseError)

def test_wrong_field_count():
    assert isinstance(parse_line(1, "2026-09-01T00:00:00Z | INFO | g | E"), ParseError)

def test_empty_line():
    assert isinstance(parse_line(1, "   \n"), ParseError)

def test_parse_timestamp_ok():
    assert parse_timestamp("2026-09-01T00:00:00Z").tzinfo is timezone.utc
