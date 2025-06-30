"""Academic_websearch_agent for finding research papers using search tools."""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


trend_researcher_agent = Agent(
    model=MODEL,
    name="trend_researcher_agent",
    instruction=prompt.TREND_RESEARCHER_PROMPT,
    output_key="destination_trends",
    tools=[google_search],
)
