from rich import print

from mew.core.detector import Detector
from mew.core.manager import Manager
from mew.ui.prompt import text_input
from mew.ui.select import select_choice


manager = Manager()


def run():

    env_type_choices = ["Python venv"]

    if Detector.conda_available():
        env_type_choices.append("Conda")

    env_type = select_choice(
        "Select environment type",
        env_type_choices
    )

    versions = Detector.detect_python_versions()

    version_choice = select_choice(
        "Select Python version",
        [v["command"] for v in versions]
    )

    name = text_input("Environment name")

    if env_type == "Python venv":
        env = manager.create_venv(name, version_choice)

    else:
        python_version = version_choice.replace("python", "")
        env = manager.create_conda(name, python_version)

    print(f"\n[green]✓ Crafted {env.name} [{env.id}][/green]")