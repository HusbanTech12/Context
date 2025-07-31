from agents import Agent, Runner
from httpx import main 
from config import config
import asyncio
agent = Agent(

    name = 'Helpful Assistant',
    instructions='You are a Helpful Assistant. Handle User Quiery & Answer easiest way Language.'
)


async def main():
 result = await Runner.run(
    agent,
    input='Hello, How are you ?',
    run_config=config,
)

 print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())