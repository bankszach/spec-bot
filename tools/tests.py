"""Test runner utilities for SoloChain."""

import subprocess
from typing import List, Optional

def run_pytest(args: Optional[List[str]] = None) -> bool:
    """Run pytest with optional arguments.
    
    Args:
        args: Optional list of pytest arguments
        
    Returns:
        True if all tests passed, False otherwise
    """
    cmd = ["pytest"]
    if args:
        cmd.extend(args)
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False 