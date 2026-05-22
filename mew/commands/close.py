import keyboard
import time
import json
import os


ACTIVE_ENV_FILE = os.path.expanduser(
    "~/.mew/active_env.txt"
)


def run():

    if not os.path.exists(ACTIVE_ENV_FILE):
        return

    with open(ACTIVE_ENV_FILE, "r") as f:
        data = json.load(f)

    backend = data.get("backend")

    if backend == "conda":

        command = "conda deactivate"

    else:

        command = "deactivate"

    keyboard.write(
        command,
        delay=0.01
    )

    time.sleep(0.05)

    keyboard.press_and_release("enter")

    os.remove(ACTIVE_ENV_FILE)