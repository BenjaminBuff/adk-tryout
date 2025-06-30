
"""Academic_newresearch_agent for finding new research lines"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro"

trend_reasoning_agent = Agent(
    model=MODEL,
    name="trend_reasoning_agent",
    instruction=prompt.trend_reasoning_PROMPT,
)
