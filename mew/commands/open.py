from rich import print
from rich.console import Console

import json
import os
import time

from mew.core.activator import (
    open_activated_shell
)

from mew.core.resolver import Resolver
from mew.registry import Registry
from mew.ui.select import select_environment


console = Console()

ACTIVE_ENV_FILE = os.path.expanduser(
    "~/.mew/active_env.txt"
)

resolver = Resolver()
registry = Registry()


def run(name_or_id: str | None = None):

    environments = registry.get_all()

    if not environments:

        print(
            "[bold #ff8800]"
            "No environments found"
            "[/bold #ff8800]"
        )

        return

    # ------------------------
    # SELECT ENV
    # ------------------------

    if not name_or_id:

        env = select_environment(
            "Select environment",
            environments
        )

    else:

        matched = resolver.resolve(name_or_id)

        if not matched:

            print(
                "[bold red]"
                "Environment not found"
                "[/bold red]"
            )

            return

        if len(matched) == 1:

            env = matched[0]

        else:

            env = select_environment(
                "Multiple environments found",
                matched
            )

    # ------------------------
    # SAVE ACTIVE ENV
    # ------------------------

    os.makedirs(
        os.path.dirname(ACTIVE_ENV_FILE),
        exist_ok=True
    )

    with open(ACTIVE_ENV_FILE, "w") as f:

        json.dump(
            {
                "id": env.id,
                "name": env.name,
                "backend": env.backend
            },
            f
        )

    # ------------------------
    # Opening Animation
    # ------------------------

    with console.status(
        "[bold #bb86fc]"
        "Preparing environment..."
        "[/bold #bb86fc]",
        spinner="dots",
        spinner_style="bold #ff8800"
    ):

        time.sleep(1)

    print(
        f"\n[bold #00ff99]"
        f"Opening {env.name} "
        f"[{env.id}]..."
        f"[/bold #00ff99]\n"
    )

    open_activated_shell(env)