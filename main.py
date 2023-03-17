import os
import sys
import platform
import logging

import distro
import dotenv
import openai



def escape_special_chars(input_str):
    return input_str.replace('?', '\?')



def generate_terminal_assistance(user_input):
    os_info = platform.system()
    if os_info == "Linux":
        os_info = distro.id(pretty=False)
    elif os_info == "Darwin":
        os_info = "macOS"
        user_input = escape_special_chars(user_input)
    
    logging.debug(f"OS: {os_info}")

    shell_info = os.environ.get('SHELL', 'Unknown shell')

    prompt = f"""
    You are an AI Assistant trained to help users with Linux shell commands. The user will provide a natural language description of what they want to do, and your task is to:

    1. Generate the appropriate Linux shell command that performs the action described.
    2. Explain what the generated command does in simple terms.
    3. Warn the user about any potential side-effects or risks associated with running the command, if applicable.

    User input: "{user_input}"
    Operating System: {os_info}
    Shell: {shell_info}
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()



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



if __name__ == "__main__":

    setup()

    logging.debug(f"{sys.argv=}")

    if len(sys.argv) == 1 or sys.argv[1] == "":
        user_input = input("Please describe the action or task you'd like to perform using the terminal: ")
    else:
        user_input = "".join(sys.argv[1:])

    result = generate_terminal_assistance(user_input)
    print(result)

    # note: instead of having a (y/N) prompt, the user will have to copy and paste the command into the terminal
