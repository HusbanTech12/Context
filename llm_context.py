from agents import Agent, Runner , FunctionTool, function_tool
from httpx import main 
from config import config
import asyncio

@function_tool(
    name_override= 'Weather Assistant',
    description_override='Fetch Weather by according given loaction'
)
async def fetch_weather(location : str) -> str :
    """
    Fetch Weather according to given location
    
     Args:
     location: Fetch waether is given location    
    """

    return f"weather in {location} is sunny"


agent = Agent(

    name = 'Helpful Assistant',
    instructions='You are a Helpful Assistant. Handle User Quiery & Answer easiest way Language.',
    tools=[fetch_weather]
)

print("Tools >>> " , agent.tools)

async def main():
 result = await Runner.run(
    agent,
    input='What is Weather in Karachi?',
    run_config=config,
)

 print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main()) 