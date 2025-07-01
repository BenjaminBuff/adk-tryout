"""Trend_evaluator_agent for validating trends found by the trend_researcher agent"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


trend_evaluator_agent = Agent(
    model=MODEL,
    name="trend_evaluator_agent",
    instruction=prompt.TREND_EVALUATOR_PROMPT,
    output_key="destination_trends_evaluated",
    tools=[google_search],
)