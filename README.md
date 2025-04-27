# SoloChain

**AI‑first LangChain template for one‑person development teams**

SoloChain is a lightweight, opinionated starter kit that lets a solo developer orchestrate
LLM agents, tools, and CI workflows from day‑zero. It focuses on real‑world productivity—not demos—so you can ship usable software while learning LangChain.

---
## Why SoloChain?
* **Agentic workflow** – Pre‑wired _planning → coding → testing → PR_ loop using LangChain`s `AgentExecutor` plus GitHub CLI.
* **Cursor‑friendly** – Repository layout and `make` targets match Cursor IDE shortcuts.
* **Model‑agnostic** – Default OpenAI GPT‑4o, but easily swap to Gemini, Claude, or local Llama via environment.
* **Trace & eval built‑in** – LangSmith tracing and unit‑test harness ready out of the box.
* **Tiny footprint** – ≤300 LOC core; no heavy web backend.

---
## Key Components
| Path | Purpose |
|------|---------|
| `agent/agent.py` | Main LangChain agent (planning + tool selection) |
| `tools/git_tools.py` | Wrapper around `gh` CLI for branch/PR ops |
| `tools/tests.py` | PyTest invocation + result parser |
| `memory/` | Conversation and episodic memory stores |
| `scripts/agent_cli.py` | TTY entry‑point for quick experiments |
| `.github/workflows/ci.yml` | Lint, test, LangSmith trace upload |

---
## Quick‑start
```bash
# 1. Fork or clone
$ git clone https://github.com/<your‑user>/solochain.git && cd solochain

# 2. Python env
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt

# 3. Environment setup
$ cp .env.example .env
$ # Edit .env and add your API keys:
$ # OPENAI_API_KEY=sk-...
$ # LANGCHAIN_API_KEY=<optional>

# 4. Fire up the CLI agent
$ python scripts/agent_cli.py "add unit tests for tools/git_tools.py"
```

---
## Development Flow
1. **Spec in ChatGPT** – Outline feature → produce task list.
2. **Sync tasks** – Paste list into `TODO.md`; run `make plan` (agent turns tasks into tracked GitHub Issues).
3. **Implement in Cursor** – Use Cursor Tab for code & tests.
4. **Augment in VS Code** – Open branch, let Copilot Agent propose refactors.
5. **PR Review** – Copilot review bot + human squash merge.
6. **CI/CD** – GitHub Actions builds & deploys (optional Heroku render).

---
## Roadmap
- [ ] GUI front‑end (Streamlit)
- [ ] Self‑hosted embedding DB (Chroma)
- [ ] Auto‑license scanner tool
- [ ] Agents that comment on Slack/Discord

---
## Requirements
* Python ≥3.11
* GitHub CLI (`brew install gh` or `scoop install gh`)
* Cursor IDE or VS Code

---
## License
MIT © 2025 Zach Banks

