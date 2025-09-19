import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# 天気を取得する
# def get_weather(city: str) -> dict:
#     """Retrieves the current weather report for a specified city.

#     Args:
#         city (str): The name of the city for which to retrieve the weather report.

#     Returns:
#         dict: status and result or error msg.
#     """
#     if city.lower() == "new york":
#         return {
#             "status": "success",
#             "report": (
#                 "The weather in New York is sunny with a temperature of 25 degrees"
#                 " Celsius (77 degrees Fahrenheit)."
#             ),
#         }
#     else:
#         return {
#             "status": "error",
#             "error_message": f"Weather information for '{city}' is not available.",
#         }

# 現在時刻を取得する
def get_current_time(tz_identifier: str) -> dict:
    """Returns the current time in a specified timezone identifier.

    Args:
        tz_identifier (str): timezone identifier like America/New_York.

    Returns:
        dict: status and result or error msg.
    """

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {tz_identifier} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

search_agent = Agent(
    name="weather_search_agent",
    model="gemini-2.5-flash",
    description="Agent to search weather using Google Search.",
    instruction="You are an agent who can use Google Search to find and answer the weather in a city.",
    tools=[google_search]
)

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city. "
        "For time queries, use the MCP time server tools to get accurate current time information for any city or timezone. "
        "When a user asks for time in a city like 'Tokyo', use the appropriate timezone identifier (e.g., 'Asia/Tokyo'). "
        "Common timezone mappings: Tokyo=Asia/Tokyo, New York=America/New_York, London=Europe/London, Paris=Europe/Paris, etc. "
        "For weather queries, use the search agent to find current weather information."
    ),
    tools=[
        agent_tool.AgentTool(agent=search_agent),
        MCPToolset(
            connection_params=StdioServerParameters(
                command="/Users/uematsuayaka/Documents/adk_handson/.venv/bin/python",
                args=["-m", "mcp_server_time", "--local-timezone=Asia/Tokyo"],
            )
        ),
    ],
)

# root_agent = Agent(
#     name="basic_search_agent",
#     model="gemini-2.5-flash",
#     description="Agent to answer questions using Google Search.",
#     instruction="I can answer your questions by searching the internet. Just ask me anything!",
#     google_search is a pre-built tool which allows the agent to perform Google searches.
#     tools=[google_search]
# )