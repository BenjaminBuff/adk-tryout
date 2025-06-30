"""Destination_Finder: Research for potential new and trendy flight destinations for the two Airlines SWISS International Air Lines and Edelweiss to fly to from ZRH and GVA"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.current_destinations.agent import current_destinations_agent
from .sub_agents.trend_researcher.agent import trend_researcher_agent
from .sub_agents.trend_evaluator.agent import trend_evaluator_agent
from .sub_agents.trend_reasoning.agent import trend_reasoning_agent

MODEL = "gemini-2.5-pro"


academic_coordinator = LlmAgent(
    name="destination_finder",
    model=MODEL,
    description=(
        "analyzing seminal papers provided by the users, "
        "providing research advice, locating current papers "
        "relevant to the seminal paper, generating suggestions "
        "for new research directions, and accessing web resources "
        "to acquire knowledge"
    ),
    instruction=prompt.ACADEMIC_COORDINATOR_PROMPT,
    output_key="destination_reasoning",
    tools=[
        AgentTool(agent=current_destinations_agent),
        AgentTool(agent=trend_researcher_agent),
        AgentTool(agent=trend_evaluator_agent),
        AgentTool(agent=trend_reasoning_agent),
    ],
)

root_agent = destination_finder
