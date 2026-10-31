#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
rm -rf htmlcov .coverage
python3 -m pytest --cov=loganalyzer --cov-report=term-missing --cov-report=html
echo
echo "HTML report: $(pwd)/htmlcov/index.html"
