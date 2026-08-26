from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware
from ai.tools.fetch_repo_names import fetch_repo_names
from ai.tools.fetch_spec_insights import fetch_spec_insights

SYSTEM_PROMPT = """You are a local github repo assistant.

 - DO NOT make up numbers, or any details.
 - MUST make sure that the data is coming from the tools you have access to.
 - Must make your output nicely formatted without using markdown.

## Capabilities

 - `fetch_repo_names`: Returns a list of the repo or repository names available. You MUST use it with the provided path only! Do not make up other path.
 - `fetch_spec_insights`: Returns a dictionary of the requested meta information from the selected repos. Adjust your required information to the user requiest. The data it returns must be specified by it's parameters.

 """

agent = create_agent(
    model="ollama:granite4.1:3b",
    tools=[fetch_repo_names, fetch_spec_insights],
    system_prompt=SYSTEM_PROMPT,
)

def invoke_agent(path, prompt):

    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": f"prompt: {prompt}, exact path argument: {path}", "path": path}]}
        )
        answer = result["messages"][-1].content_blocks[0]["text"]

        if len(answer) == 0:
            raise Exception("There was an error with the model")
            

        return answer

    except Exception as e:
        return e