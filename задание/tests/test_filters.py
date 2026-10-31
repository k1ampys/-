from datetime import datetime, timezone
from loganalyzer.parser import Record
from loganalyzer.filters import Filters

def rec(ts, lvl="INFO", src="s"):
    return Record(datetime.fromisoformat(ts).replace(tzinfo=timezone.utc), lvl, src, "E", "m")

def test_boundaries():
    f = Filters(from_ts=datetime(2026,9,1,0,0,0,tzinfo=timezone.utc), to_ts=datetime(2026,9,2,0,0,0,tzinfo=timezone.utc))
    assert f.matches(rec("2026-09-01T00:00:00"))
    assert not f.matches(rec("2026-09-02T00:00:00"))

def test_level_source_combination():
    f = Filters(level="ERROR", source="gateway")
    assert f.matches(rec("2026-09-01T00:00:00", "ERROR", "gateway"))
    assert not f.matches(rec("2026-09-01T00:00:00", "INFO", "gateway"))
