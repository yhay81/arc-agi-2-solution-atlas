import sys
from pathlib import Path

from arc_agi_2_atlas.cli import main


def test_cli_verifies_current_corpus(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["arc-atlas", "verify", "--solutions", "solutions", "--expected-tasks", "1"],
    )
    assert main() == 0
    assert "tasks=1 pairs=8 passed=8 failed=0" in capsys.readouterr().out


def test_cli_rejects_wrong_task_count(monkeypatch, capsys, tmp_path: Path) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["arc-atlas", "verify", "--solutions", str(tmp_path), "--expected-tasks", "1120"],
    )
    assert main() == 1
    output = capsys.readouterr().out
    assert "expected 1120 tasks, found 0" in output
