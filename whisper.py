# https://platform.openai.com/docs/guides/speech-to-text

import openai

file = open("./talking.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)
