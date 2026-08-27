from langchain.agents import create_agent
from ai.tools.fetch_repo_names import fetch_repo_names
from ai.tools.fetch_spec_insights import fetch_spec_insights
from ai.tools.generate_metadata import generate_metadata
from ai.system_instructions import get_sys_instructions

SYSTEM_INSTRUCTIONS = get_sys_instructions()

agent = create_agent(
    model="ollama:granite4.1:3b",
    tools=[fetch_repo_names, fetch_spec_insights, generate_metadata],
    system_prompt=SYSTEM_INSTRUCTIONS,
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