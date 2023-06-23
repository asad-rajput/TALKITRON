import os
from glob import glob
from pyaiml21 import Kernel

base_path = os.path.join(os.getcwd()+'/polls/backend/')

myBot = Kernel()
for files in glob('files/*.aiml'):
    myBot.learn_aiml(files)


def generate_response(message):
    text = str(message)
    if text.lower() == "bye" or text.lower() == "good bye":
        return "Bye"

    with open(base_path+"store.txt", "a") as file:
        file.write(f"User said: {text}\n")

    response = myBot.respond(text, "Asad")

    with open(base_path+"store.txt", "a") as file:
        file.write(f"Bot responded: {response}\n")

    return response
