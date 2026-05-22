from rich import print
from rich.console import Console

from mew.core.detector import Detector
from mew.core.manager import Manager
from mew.ui.prompt import text_input
from mew.ui.select import select_choice


console = Console()

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

    # ------------------------
    # Craft Animation
    # ------------------------

    with console.status(
        "[bold magenta]Crafting environment...[/bold magenta]",
        spinner="arc",
        spinner_style="bold #ff8800"
    ):

        if env_type == "Python venv":

            env = manager.create_venv(
                name,
                version_choice
            )

        else:

            python_version = (
                version_choice
                .replace("python", "")
            )

            env = manager.create_conda(
                name,
                python_version
            )

    # ------------------------
    # Success Message
    # ------------------------

    print(
        f"\n[bold #00ff99]"
        f"Environment crafted successfully"
        f"[/bold #00ff99]"
    )

    print(
        f"[bold #bb86fc]Name:[/bold #bb86fc] "
        f"[bold white]{env.name}[/bold white]"
    )

    print(
        f"[bold #ff8800]ID:[/bold #ff8800] "
        f"[bold white]{env.id}[/bold white]\n"
    )