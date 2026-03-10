#!/usr/bin/env python3
"""
Market Research Assistant - Claude Agent
A specialized agent for analyzing companies, industries, and competitors.
"""

import os
import sys
from anthropic import Anthropic

# Load .env file
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(_env_path):
    with open(_env_path) as _f:
        for _line in _f:
            if "=" in _line and not _line.startswith("#"):
                _k, _v = _line.strip().split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

# API Configuration
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
CLAUDE_BASE_URL = os.getenv("CLAUDE_BASE_URL")

# System prompt for the agent
SYSTEM_PROMPT = """You are a market research assistant helping analyze companies, industries, and competitors.

Instructions:
When given a question, provide a short factual answer based on your knowledge.

Output:
Start with a verdict prefix: either "✅ FACT:" or "❌ UNKNOWN:"
Follow with a concise one-sentence explanation."""


class MarketResearchAgent:
    """Claude-powered market research assistant."""

    def __init__(self, api_key: str = CLAUDE_API_KEY):
        """Initialize the agent with API key."""
        self.client = Anthropic(api_key=api_key, base_url=CLAUDE_BASE_URL)
        self.model = "claude-sonnet-4-6"
        self.system_prompt = SYSTEM_PROMPT
        self.conversation_history = []

    def ask(self, question: str) -> str:
        """
        Ask the agent a market research question.

        Args:
            question: The question to ask

        Returns:
            The agent's response with verdict prefix
        """
        self.conversation_history.append({"role": "user", "content": question})
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=self.system_prompt,
                messages=self.conversation_history
            )
            response = message.content[0].text
            self.conversation_history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            self.conversation_history.pop()
            import traceback; traceback.print_exc()
            return f"❌ ERROR: {str(e)}"

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []

    def chat(self):
        """Start an interactive chat session."""
        print("=" * 60)
        print("Market Research Assistant - Claude Agent")
        print("=" * 60)
        print("Ask questions about companies, industries, and competitors.")
        print("Type 'quit' or 'exit' to end the session. Type 'clear' to reset memory.\n")

        while True:
            try:
                question = input("You: ").strip()

                if question.lower() in ['quit', 'exit', 'q']:
                    print("\nGoodbye!")
                    break

                if question.lower() == 'clear':
                    self.clear_history()
                    print("Memory cleared.\n")
                    continue

                if not question:
                    continue

                print("\nAgent:", end=" ")
                response = self.ask(question)
                print(response)
                print()

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\n❌ ERROR: {e}\n")


def main():
    """Main entry point for the agent."""
    agent = MarketResearchAgent()

    # Example usage
    print("Example Query:")
    print("-" * 60)
    example_question = "What is the main competitor of Tesla in the EV market?"
    print(f"Question: {example_question}")
    print(f"Answer: {agent.ask(example_question)}")
    print("-" * 60)
    print()

    # Start interactive chat (only when running in a terminal)
    if sys.stdin.isatty():
        agent.chat()


if __name__ == "__main__":
    main()
