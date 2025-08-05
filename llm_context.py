from agents import Agent, Runner, function_tool
from config import config
import asyncio  # ✅ You need this

@function_tool(
    name_override='weather_assistant',
    description_override='Fetch Weather by according given location'
)
def fetch_weather(location: str) -> str:
    """
    Fetch weather according to given location

    Args:
        location: Fetch weather in the given location    
    """
    return f"weather in {location} is sunny"

agent = Agent(
    name='Helpful Assistant',
    instructions='You are a Helpful Assistant. Handle User Quiery & Answer easiest way Language.',
    tools=[fetch_weather]
)

# ✅ Wrap it in async def
async def main():
  result = await Runner.run(
        agent,
        input='What is Weather in Karachi?',
        run_config=config,
    )
    
  print(result)

# ✅ Proper async run
if __name__ == "__main__":
    asyncio.run(main())
