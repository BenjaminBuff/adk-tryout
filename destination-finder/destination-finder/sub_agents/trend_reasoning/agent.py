
"""Trend_reasoning_agent for writing a reasoning about why this new destination(s) would make sense to look at for SWISS International Air Lines or Edelweiss Air."""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro"

trend_reasoning_agent = Agent(
    model=MODEL,
    name="trend_reasoning_agent",
    output_key="destination_reasoning",
    instruction=prompt.trend_reasoning_PROMPT,
)
