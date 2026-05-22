import subprocess
import shutil
from pathlib import Path

from rich import print
from InquirerPy import inquirer

from mew.core.ids import generate_id
from mew.core.resolver import Resolver
from mew.registry import Registry
from mew.models.environment import Environment
from mew.ui.select import select_environment


resolver = Resolver()
registry = Registry()


def run(name_or_id: str | None = None):

    environments = registry.get_all()

    if not environments:

        print(
            "[yellow]No environments found[/yellow]"
        )

        return

    # ------------------------
    # SELECT SOURCE ENV
    # ------------------------

    if not name_or_id:

        source_env = select_environment(
            "Select environment to clone",
            environments
        )

    else:

        matched = resolver.resolve(name_or_id)

        if not matched:

            print(
                "[red]Environment not found[/red]"
            )

            return

        if len(matched) == 1:

            source_env = matched[0]

        else:

            source_env = select_environment(
                "Multiple environments found",
                matched
            )

    # ------------------------
    # NEW ENV NAME
    # ------------------------

    new_name = inquirer.text(
        message="New environment name:"
    ).execute()

    new_id = generate_id()

    # ------------------------
    # CLONE VENV
    # ------------------------

    if source_env.backend == "venv":

        source_path = Path(source_env.path)

        target_path = (
            source_path.parent /
            f"{new_name}-{new_id}"
        )

        print(
            "\n[cyan]Cloning venv...[/cyan]\n"
        )

        shutil.copytree(
            source_path,
            target_path
        )

        new_env = Environment(
            id=new_id,
            name=new_name,
            backend="venv",
            python_version=source_env.python_version,
            path=str(target_path),
            created_at="cloned"
        )

    # ------------------------
    # CLONE CONDA
    # ------------------------

    else:

        source_conda = (
            f"{source_env.name}-{source_env.id}"
        )

        target_conda = (
            f"{new_name}-{new_id}"
        )

        print(
            "\n[cyan]Cloning conda env...[/cyan]\n"
        )

        subprocess.run(
            [
                "conda",
                "create",
                "--name",
                target_conda,
                "--clone",
                source_conda,
                "-y"
            ]
        )

        new_env = Environment(
            id=new_id,
            name=new_name,
            backend="conda",
            python_version=source_env.python_version,
            path=f"conda:{target_conda}",
            created_at="cloned"
        )

    # ------------------------
    # SAVE
    # ------------------------

    registry.add(new_env)

    print(
        f"\n[green]✓ Cloned "
        f"{source_env.name} "
        f"→ "
        f"{new_name} "
        f"[{new_id}][/green]"
    )