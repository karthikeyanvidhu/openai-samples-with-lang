import os
from dotenv import load_dotenv

from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
	raise RuntimeError("Set OPENAI_API_KEY in your environment or ai-samples/.env")

llm = OpenAI(temperature=0.0)

tools = load_tools(['wikipedia','llm-math'], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

prompt = input('Wikipedia Research Task')

agent.run(prompt)