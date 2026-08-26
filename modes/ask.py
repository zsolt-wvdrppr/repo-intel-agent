from ai.agent import invoke_agent

def ask(args):

        question = args.question
        path = args.path

        try:
            if len(question) == 0:
                  raise Exception("Missing question!")

            if len(path) == 0:
                  raise Exception("Missing path!")

            answer = invoke_agent(path, question)

            return answer

        except Exception as e:
            return f"\n\nThere was an error:{e}\n\n"
            



