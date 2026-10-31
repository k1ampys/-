import argparse
import os
import sys
from .parser import parse_line, ParseError, Record, parse_timestamp
from .filters import Filters
from .aggregator import Aggregator
from .report import render_text, write_json, write_csv

def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="loganalyzer")
    p.add_argument("--input", "-i", required=True)
    p.add_argument("--from", dest="from_ts")
    p.add_argument("--to", dest="to_ts")
    p.add_argument("--level", choices=["TRACE", "DEBUG", "INFO", "WARN", "ERROR"])
    p.add_argument("--source")
    p.add_argument("--top", type=int, default=5)
    p.add_argument("--format", choices=["text", "json", "csv"], default="text")
    p.add_argument("--output", "-o")
    return p

def main(argv=None) -> int:
    args = build_argparser().parse_args(argv)
    if not os.path.exists(args.input):
        print(f"error: input file not found: {args.input}", file=sys.stderr); return 2
    if os.path.getsize(args.input) == 0:
        print(f"error: input file is empty: {args.input}", file=sys.stderr); return 2
    if args.format in ("json", "csv") and not args.output:
        print("error: --output is required for json/csv", file=sys.stderr); return 2
    try:
        from_ts = parse_timestamp(args.from_ts) if args.from_ts else None
        to_ts = parse_timestamp(args.to_ts) if args.to_ts else None
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr); return 2
    if from_ts and to_ts and from_ts > to_ts:
        print("error: --from must be <= --to", file=sys.stderr); return 2

    filters = Filters(from_ts=from_ts, to_ts=to_ts, level=args.level, source=args.source)
    agg = Aggregator(top_n=max(0, args.top))
    invalid_lines = []

    with open(args.input, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            agg.total_lines += 1
            res = parse_line(line_no, raw)
            if isinstance(res, ParseError):
                agg.add_invalid()
                invalid_lines.append(res)
                continue
            agg.add_valid(res, filters.matches(res))

    if args.format == "text": render_text(agg, invalid_lines)
    elif args.format == "json":
        write_json(args.output, agg, invalid_lines); print(f"written: {args.output}")
    else:
        write_csv(args.output, agg, invalid_lines); print(f"written: {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
