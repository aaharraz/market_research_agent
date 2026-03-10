# Market Research Assistant - Claude Agent

A specialized Claude-powered agent for analyzing companies, industries, and competitors.

## Features

- Uses Claude Opus 4.5 for market research analysis
- Provides factual answers with verdict prefixes (✅ FACT: or ❌ UNKNOWN:)
- Interactive chat interface
- Concise, one-sentence responses

## Python env
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install xyz

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the agent in interactive chat mode:
```bash
python market_research_agent.py
```

### Programmatic Usage

```python
from market_research_agent import MarketResearchAgent

agent = MarketResearchAgent()
response = agent.ask("What is the main competitor of Tesla?")
print(response)
```

## Example Queries

- "What is the main competitor of Tesla in the EV market?"
- "Who are the major players in the cloud computing industry?"
- "What industry does Salesforce operate in?"
- "What is Amazon's primary revenue source?"

## Configuration

The API key is configured in the script. To use a different key, you can either:
- Modify the `CLAUDE_API_KEY` variable in the script
- Pass a different key when initializing: `MarketResearchAgent(api_key="your-key")`

## Output Format

All responses follow this format:
- **✅ FACT:** Followed by a factual answer
- **❌ UNKNOWN:** When the information is uncertain or unavailable
