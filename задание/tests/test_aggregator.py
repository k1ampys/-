from datetime import datetime, timezone
from loganalyzer.parser import Record
from loganalyzer.aggregator import Aggregator

def r(lvl, src, code):
    return Record(datetime(2026,9,1,tzinfo=timezone.utc), lvl, src, code, "m")

def test_counts_and_top():
    a = Aggregator(top_n=2)
    a.add_valid(r("ERROR","gateway","HTTP_502"), True)
    a.add_valid(r("ERROR","payment-worker","PAYMENT_TIMEOUT"), True)
    a.add_valid(r("ERROR","payment-worker","PAYMENT_TIMEOUT"), True)
    d = a.as_dict()
    assert d["matched_events"] == 3
    assert d["top_error_codes"][0]["count"] == 2
