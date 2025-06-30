"""Current_destinations_agent for finding destinations of SWISS International Airlines and Edelweiss Air"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"

current_destinations_agent = Agent(
    model=MODEL,
    name="current-destinations-agent",
    instruction=prompt.CURRENT_DESTINATIONS_PROMPT,
    output_key="current_destinations",
    tools=[google_search],
)
