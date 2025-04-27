#!/usr/bin/env python3
"""Command-line interface for SoloChain agent."""

import sys
from agent.agent import handle_task

def main():
    """Run the SoloChain agent CLI."""
    if len(sys.argv) < 2:
        print("Usage: python agent_cli.py <task>")
        sys.exit(1)
        
    task = " ".join(sys.argv[1:])
    try:
        result = handle_task(task)
        print("\nAgent Response:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 