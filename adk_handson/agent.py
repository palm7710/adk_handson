import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

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

root_agent = Agent(
    name="enjoy_chat_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to chat with user."
    ),
    instruction=(
        "You are an agent who enjoys chatting with users."
    ),
    tools=[get_current_time],
)