import subprocess, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "agent_cli.py"

def test_agent_end_to_end():
    """Agent should find its own handle_task definition."""
    cmd = [sys.executable, CLI, "Search for def handle_task in *.py and show path"]
    out = subprocess.check_output(cmd, text=True)
    assert "agent/agent.py" in out, "handle_task path missing in agent reply" 