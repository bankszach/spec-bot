"""LangChain agent that orchestrates SoloChain tasks."""

import os
from pathlib import Path
from typing import List, Optional
from langchain.agents import AgentExecutor, AgentType, initialize_agent
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from tools.git_tools import open_branch, open_pr
from tools.tests import run_pytest

def _check_api_key():
    """Check if OpenAI API key is set."""
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError(
            "OPENAI_API_KEY not found. Please set it in your .env file or environment."
        )
    print(f"Found API key starting with: {key[:8]}...")

def _create_llm():
    """Create and return the LLM instance."""
    _check_api_key()
    return ChatOpenAI(model_name="gpt-4", temperature=0)

def _create_tools() -> List[Tool]:
    """Create and return the list of tools."""
    return [
        Tool(
            name="Run tests",
            func=run_pytest,
            description="Run pytest and return summary"
        ),
        Tool(
            name="Open branch",
            func=open_branch,
            description="Create and checkout a new git branch"
        ),
        Tool(
            name="Open PR",
            func=open_pr,
            description="Open a GitHub pull request for current branch"
        ),
    ]

def handle_task(task: str) -> str:
    """Entry point for external callers (CLI/HTTP).
    
    Args:
        task: The task description to execute
        
    Returns:
        The agent's response
    """
    print("Loading environment...")
    from dotenv import load_dotenv
    load_dotenv()
    
    print("Creating LLM...")
    llm = _create_llm()
    print("Creating tools...")
    tools = _create_tools()
    
    print("Setting up agent...")
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    print("Running agent...")
    return agent.run(task) 