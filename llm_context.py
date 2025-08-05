from agents import Agent, Runner, function_tool
from config import config
import asyncio  # ✅ You need this



@function_tool
def sum(a:int , b:int) -> int :
   """
   Sum of Two numbers
   
   Args:

   a: integer number
   b: integer number
   """ 
   return a + b

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
    tools=[fetch_weather , sum],
    tool_use_behavior='stop_on_first_tool'

    
)

# ✅ Wrap it in async def
async def main():
  result = await Runner.run(
        agent,
        input='What is Weather in Karachi & sum of two num 2 and 5',
        run_config=config,
    )

  print(result.final_output)

# ✅ Proper async run
if __name__ == "__main__":
    asyncio.run(main())
