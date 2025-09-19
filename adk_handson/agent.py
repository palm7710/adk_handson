import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

# 天気を取得する
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

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

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are an agent who enjoys chatting with users."
    ),
    tools=[get_weather, get_current_time],
)