import csv
import json
import sys
from .aggregator import Aggregator

def render_text(agg: Aggregator, invalid_lines: list, out=None) -> None:
    if out is None:
        out = sys.stdout
    d = agg.as_dict()
    
    def p(text):
        out.write(text + "\n")

    p("=" * 60)
    p("LOG ANALYSIS SUMMARY")
    p("=" * 60)
    p(f"total lines        : {d['total_lines']}")
    p(f"valid lines        : {d['valid_lines']}")
    p(f"invalid lines      : {d['invalid_lines']}")
    p(f"matched after filter: {d['matched_events']}")
    p("-" * 60)
    p("by level:")
    for k, v in d["by_level"].items(): p(f"  {k:<6} {v}")
    p("by source:")
    for k, v in d["by_source"].items(): p(f"  {k:<16} {v}")
    p(f"top-{agg.top_n} error codes:")
    for item in d["top_error_codes"]: p(f"  {item['code']:<24} {item['count']}")
    if invalid_lines:
        p("-" * 60)
        p(f"invalid line numbers (first 20): {[x.line_no for x in invalid_lines[:20]]}")
    out.flush()

def write_json(path: str, agg: Aggregator, invalid_lines: list) -> None:
    payload = agg.as_dict()
    payload["invalid_line_numbers"] = [x.line_no for x in invalid_lines]
    with open(path, "w", encoding="utf-8") as f: json.dump(payload, f, ensure_ascii=False, indent=2)

def write_csv(path: str, agg: Aggregator, invalid_lines: list) -> None:
    d = agg.as_dict()
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["metric", "key", "value"])
        for k in ("total_lines", "valid_lines", "invalid_lines", "matched_events"): w.writerow([k, "", d[k]])
        for k, v in d["by_level"].items(): w.writerow(["by_level", k, v])
        for k, v in d["by_source"].items(): w.writerow(["by_source", k, v])
        for item in d["top_error_codes"]: w.writerow(["top_error_code", item["code"], item["count"]])
        for e in invalid_lines: w.writerow(["invalid_line", e.line_no, e.reason])
