from loganalyzer.cli import main

def test_sample_processing(tmp_path, capsys):
    data = (
        "2026-09-01T00:00:00Z | INFO | auth-api | AUTH_LOGIN_OK | ok\n"
        "2026-09-01T00:00:00Z | ERROR | gateway | HTTP_502 | bad\n"
        "not-a-timestamp | ERROR | orders-api | X | x\n"
        "2026-09-01T00:00:00Z | NOTICE | g | X | x\n"
    )
    f = tmp_path/"s.log"; f.write_text(data)
    main(["--input", str(f), "--level", "ERROR"])
    captured = capsys.readouterr()
    assert "matched after filter: 1" in (captured.out + captured.err)
