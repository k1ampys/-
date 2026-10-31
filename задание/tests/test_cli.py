from loganalyzer.cli import main
VALID = "2026-09-01T00:00:00Z | ERROR | gateway | HTTP_502 | x\n"

def test_missing_file(tmp_path, capsys):
    assert main(["--input", str(tmp_path/"nope.log")]) == 2

def test_text_run(tmp_path, capsys):
    f = tmp_path/"a.log"; f.write_text(VALID + "broken line\n")
    assert main(["--input", str(f)]) == 0
    captured = capsys.readouterr()
    # Ищем текст либо в stdout, либо в общем выводе (на случай особенностей Python 3.14)
    assert "invalid line numbers" in (captured.out + captured.err)

def test_json_and_csv(tmp_path):
    f = tmp_path/"a.log"; f.write_text(VALID)
    assert main(["--input", str(f), "--format", "json", "--output", str(tmp_path/"o.json")]) == 0
    assert main(["--input", str(f), "--format", "csv",  "--output", str(tmp_path/"o.csv")]) == 0
