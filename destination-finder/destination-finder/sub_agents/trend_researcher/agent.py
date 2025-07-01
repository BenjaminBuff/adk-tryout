"""Trend_researcher_agent for finding new travel trend destinations in the internet."""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


trend_researcher_agent = Agent(
    model=MODEL,
    name="trend_researcher_agent",
    instruction=prompt.TREND_RESEARCHER_PROMPT,
    output_key="trending_destinations_raw",
    tools=[google_search],
)
