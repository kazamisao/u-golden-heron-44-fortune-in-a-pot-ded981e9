"""Tests for the fortune-in-a-pot entry program (main.py).

Behavior: running `python3 main.py` with MAKEFUN_OUTPUT_DIR set writes
exactly one fortune line to $MAKEFUN_OUTPUT_DIR/entry.txt:
1-120 characters, a single line, not only whitespace, deterministic
(two runs produce identical bytes), no network.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent
MAIN = REPO / "main.py"


def run_program(out_dir: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["MAKEFUN_OUTPUT_DIR"] = str(out_dir)
    return subprocess.run(
        [sys.executable, str(MAIN)],
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_entry_file_exists_and_is_valid():
    """entry.txt exists, is 1-120 chars, one line, not only whitespace."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        result = run_program(out)
        assert result.returncode == 0, f"main.py failed: {result.stderr}"
        entry = out / "entry.txt"
        assert entry.exists(), "entry.txt was not written"
        text = entry.read_text(encoding="utf-8")
        assert 1 <= len(text) <= 120, f"length {len(text)} outside 1-120"
        assert text.strip(), "entry is only whitespace"
        assert "\n" not in text.strip(), "entry must be a single line"


def test_deterministic_two_runs_identical():
    """Two runs write byte-identical entry.txt."""
    with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
        out1, out2 = Path(tmp1), Path(tmp2)
        assert run_program(out1).returncode == 0
        assert run_program(out2).returncode == 0
        b1 = (out1 / "entry.txt").read_bytes()
        b2 = (out2 / "entry.txt").read_bytes()
        assert b1 == b2, "two runs produced different entry.txt bytes"


def test_no_trailing_newline_inflates_length():
    """The written text has no trailing newline (length counts the fortune only)."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        assert run_program(out).returncode == 0
        text = (out / "entry.txt").read_text(encoding="utf-8")
        assert text == text.strip(), "entry has leading/trailing whitespace"


def test_fortune_names_leaf_and_photographer():
    """The fortune is about the next leaf and its documented debut.

    The joke turns on the leaf arriving like a promotion and the keeper
    booking a photographer for it, so both halves must be present.
    """
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        assert run_program(out).returncode == 0
        text = (out / "entry.txt").read_text(encoding="utf-8")
        assert "leaf" in text, "fortune never mentions the leaf"
        assert "photographer" in text, "fortune never mentions the photographer"
        assert "promotion" in text, "fortune never frames the leaf as a promotion"


def test_program_uses_stdlib_only():
    """main.py imports only the standard library (os, pathlib)."""
    import ast

    tree = ast.parse(MAIN.read_text(encoding="utf-8"))
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    assert imports <= {"os", "pathlib"}, f"non-stdlib imports: {imports}"
