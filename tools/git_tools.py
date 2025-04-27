"""GitHub CLI wrapper tools for SoloChain."""

import subprocess
from typing import Optional

def open_branch(branch_name: str) -> bool:
    """Create and switch to a new Git branch.
    
    Args:
        branch_name: Name of the branch to create
        
    Returns:
        True if successful, False otherwise
    """
    try:
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def open_pr(title: str, body: Optional[str] = None) -> bool:
    """Create a GitHub pull request.
    
    Args:
        title: PR title
        body: Optional PR description
        
    Returns:
        True if successful, False otherwise
    """
    try:
        cmd = ["gh", "pr", "create", "--title", title]
        if body:
            cmd.extend(["--body", body])
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False 