from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware
from ai.tools.fetch_repo_names import fetch_repo_names

# SYSTEM_PROMPT = """You are a local github repo assistant.

# ## Capabilities

# - `fetch_repo_names`: Returns an array of the repo or repository names available.

# """

agent = create_agent(
    model="ollama:granite4.1:3b",
    tools=[fetch_repo_names],
    system_prompt="Local git repository assistant",
)

def invoke_agent(prompt):
    result = agent.invoke(
        {"messages": [{"role": "user", "content": prompt}]}
    )
    answer = result["messages"][-1].content_blocks[0]["text"]
    return answer