#!/usr/bin/env python3
"""
Example usage of the Market Research Agent
"""

from agent import MarketResearchAgent


def main():
    # Initialize the agent
    agent = MarketResearchAgent()

    # Example questions
    questions = [
        "What is the main competitor of Tesla in the EV market?",
        "Who founded Microsoft?",
        "What industry does Stripe operate in?",
        "What is the market cap of Apple?",
        "Who are the Big Tech companies?",
    ]

    print("Market Research Agent - Example Queries")
    print("=" * 60)
    print()

    for question in questions:
        print(f"Q: {question}")
        response = agent.ask(question)
        print(f"A: {response}")
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()
