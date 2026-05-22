import os
import subprocess
import shellingham

from rich import print


def open_activated_shell(env):

    shell, _ = shellingham.detect_shell()

    # ------------------------
    # CLEAN NAME
    # ------------------------

    env.name = env.name.strip()

    # ------------------------
    # INVALID SPACE CHECK
    # ------------------------

    if env.backend == "conda":

        if " " in env.name:

            print(
                "\n[bold red]"
                "Conda environment names "
                "cannot contain spaces"
                "[/bold red]"
            )

            print(
                "[bold #ff8800]"
                "Use hyphen (-) or underscore (_)"
                "[/bold #ff8800]\n"
            )

            return

    # ------------------------
    # VENV
    # ------------------------

    if env.backend == "venv":

        # WINDOWS
        if os.name == "nt":

            # PowerShell
            if "powershell" in shell.lower():

                activate_script = (
                    f'{env.path}\\Scripts\\Activate.ps1'
                )

                subprocess.run([
                    "powershell",
                    "-NoExit",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-Command",
                    f'& "{activate_script}"'
                ])

            # CMD
            else:

                activate_script = (
                    f'{env.path}\\Scripts\\activate.bat'
                )

                subprocess.run([
                    "cmd",
                    "/K",
                    activate_script
                ])

        # LINUX / MAC
        else:

            activate_script = (
                f'{env.path}/bin/activate'
            )

            subprocess.run([
                "bash",
                "-c",
                f"source {activate_script} && exec bash"
            ])

    # ------------------------
    # CONDA
    # ------------------------

    elif env.backend == "conda":

        conda_env = env.path.replace(
            "conda:",
            ""
        ).strip()

        # WINDOWS
        if os.name == "nt":

            subprocess.run([
                "powershell",
                "-NoExit",
                "-Command",
                f"conda activate {conda_env}"
            ])

        # LINUX / MAC
        else:

            subprocess.run([
                "bash",
                "-c",
                f"conda activate {conda_env} && exec bash"
            ])