# An ai assistant in your CLI.

But it knows what's on your system and can help you get things done.

Make sure to replace the API key with your openAI API key.

My favorite usage. No more ffmpeg Googling:

Below is the ChatGPT generated Readme with some edits.

This is a simple Python script that uses the power of prompt engineering and a bit of imagination to use the revChatGPT library to build a ChatGPT powered AI assistant that can interact with users via a terminal interface and has access to interact with the user's programs and files.

The script reads an initial prompt from the system_prompt.txt file and initializes a Chatbot object using the OpenAI API key provided. The chatbot then enters a loop where it prompts the user for input and sends it to the OpenAI API to retrieve a response.

If the response contains the @Backend string, the script extracts

the command to be executed from the response, runs the command using subprocess, captures the output and exit code, and sends the results back to the chatbot for interpretation.

If the response contains the @Human string, the script extracts the response from the chatbot and prints it to the terminal.

# Requirements

Python 3 revChatGPT library An OpenAI API key

# Usage

Clone this repository to your local machine.

Install the required dependencies using pip. pip install revChatGPT

Add your OpenAI API key to the api_key variable in the assistant.py script.

Run the assistant.py script using python.

Type your query or question when prompted by the script.

To exit the script, type "exit" or "quit" at the prompt.

# Disclaimer

This code is provided as-is and is not guaranteed to work or be suitable for any particular purpose. The author assumes no responsibility for any damages or losses that may result from the use of this code. Use at your own risk. As soon as a query is processed, ChatGPT executes the command. Be careful on what you ask it to do. Don't run it as root and don't ask it to rm -rf / . You have been warned.
