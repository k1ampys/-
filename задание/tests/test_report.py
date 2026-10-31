import json, csv, sys
from datetime import datetime, timezone
from loganalyzer.parser import Record, ParseError
from loganalyzer.aggregator import Aggregator
from loganalyzer.report import write_json, write_csv, render_text

def make_agg():
    a = Aggregator()
    a.total_lines = 2
    a.add_valid(Record(datetime(2026,9,1,tzinfo=timezone.utc),"ERROR","gateway","HTTP_502","m"), True)
    a.add_invalid()
    return a

def test_write_json(tmp_path):
    p = tmp_path/"out.json"
    write_json(str(p), make_agg(), [ParseError(2,"bad","x")])
    data = json.loads(p.read_text())
    assert data["total_lines"] == 2

def test_write_csv(tmp_path):
    p = tmp_path/"out.csv"
    write_csv(str(p), make_agg(), [])
    rows = list(csv.reader(p.read_text().splitlines()))
    assert rows[0] == ["metric","key","value"]

def test_render_text(capsys):
    render_text(make_agg(), [], out=sys.stdout)
    assert "LOG ANALYSIS SUMMARY" in capsys.readouterr().out
