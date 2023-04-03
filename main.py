import os
import sys
import platform
import logging
from dataclasses import dataclass

import distro
import dotenv
import openai



# TEMPERATURE = 0.5
TEMPERATURE = 0.3



####################
def generate_prompt(user_input):

    # os_info = platform.system()
    os_info = distro.name(pretty=True)
    shell = os.environ.get('SHELL')
    shell_version = os.popen(f"{shell} --version").read().strip()

#     prompt = f"""
# You are an AI Assistant trained to help users with Linux shell commands. The user will provide a natural language description of what they want to do, and your task is to (1) generate the appropriate Linux shell command that performs the action described, (2) explain what the generated command does in simple terms, and (3) warn the user about any potential side-effects or risks associated with running the command, if applicable.

# You should reply in this format:
# COMMAND: <command>
# EXPLANATION: <detailed description of the given command>
# WARNING: <warnings and side-effects>

# If you are not confident about what the user is asking for, or need clarification for any reason, you will ask the user to clarify or rephrase their request. Similarly, if you are unable to generate a suitable command that satisfies the user's request, you will ask the user to clarify or rephrase their request.

# If clarification is needed you will reply with:
# CLARIFICATION NEEDED: <request to user>

# ---

# This is the user's machine information:
# Operating System: {os_info}
# Shell: {shell}
# Shell version: {shell_version}

# User input: "{user_input}"
# """
    prompt = f"""
You are an AI Assistant trained to help users with Linux shell commands. The user provides a description of their desired action, and your task is to generate the appropriate shell command, explain it, and warn about potential side-effects or risks.

Reply in this format:
COMMAND: <command>
EXPLANATION: <description>
WARNING: <warnings and side-effects>

If clarification is needed, reply with:
CLARIFICATION NEEDED: <request to user>

If the user's system is not supported, reply with:
UNSUPPORTED SYSTEM: <request to user>

User's machine information:
Operating System: {os_info}
Shell: {shell}
Shell Version: {shell_version}

User input: "{user_input}"
"""
# If you are unable to generate a suitable command, reply with:
# UNABLE TO GENERATE COMMAND: <request to user>

    logging.debug(f"Prompt: {prompt}")

    # while True:

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=TEMPERATURE,
    )

    logging.debug(f"Response: {response}")

    response_text = response.choices[0].text.strip()

        # # if response_text starts with "CLARIFICATION NEEDED:":
        # if not response_text.startswith("CLARIFICATION NEEDED:"):
        #     break
        # if response_text.startswith("CLARIFICATION NEEDED:"):
        #     print("UNABLE TO GENERATE COMMAND: Clarification needed!!")

        # logging.debug("Clarification needed!!")

        # # prompt += response_text + "\n"

        # print(response_text)
        # print()
        # user_clarification = input("Please clarify your request: ")

        # prompt += f"""To clarify: {user_clarification}"""



        


    # return response
    return response_text

    


####################
def setup():
    logging.basicConfig(
            level=logging.DEBUG,
            handlers=[logging.StreamHandler()],
            format="%(name)s [%(levelname)s] (%(filename)s @ %(lineno)d) %(message)s")
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    dotenv.load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable in a .env file.")

    openai.api_key = api_key




####################
if __name__ == "__main__":

    setup()

    logging.debug(f"{sys.argv=}")

    if len(sys.argv) == 1 or sys.argv[1] == "":
        try:
            user_input = input("Please describe the action or task you'd like to perform using the terminal: ")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)
    else:
        user_input = "".join(sys.argv[1:])

    result = generate_prompt(user_input)
    print(result)

    # note: instead of having a (y/N) prompt, the user will have to copy and paste the command into the terminal
