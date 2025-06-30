"""Destination_Finder: Research for potential new and trendy flight destinations for the two Airlines SWISS International Air Lines and Edelweiss to fly to from ZRH and GVA"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.current_destinations.agent import current_destinations_agent
from .sub_agents.trend_researcher.agent import trend_researcher_agent
from .sub_agents.trend_evaluator.agent import trend_evaluator_agent
from .sub_agents.trend_reasoning.agent import trend_reasoning_agent

MODEL = "gemini-2.5-pro"


destination_finder = LlmAgent(
    name="destination_finder",
    model=MODEL,
    description=(
        "finding new trend travel destinations and evaluating if those would make sense to be added to the flight schedule of SWISS International Air Lines or Edelweiss Air."
    ),
    instruction=prompt.ROOT_AGENT_INSTR,
    output_key="destination_reasoning",
    tools=[
        AgentTool(agent=current_destinations_agent),
        AgentTool(agent=trend_researcher_agent),
        AgentTool(agent=trend_evaluator_agent),
        AgentTool(agent=trend_reasoning_agent),
    ],
)

root_agent = destination_finder
