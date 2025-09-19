from google.adk.agents import Agent

root_agent = Agent(
    name="enjoy_chat_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to chat with user."
    ),
    instruction=(
        "You are an agent who enjoy chatting with users."
    ),
)