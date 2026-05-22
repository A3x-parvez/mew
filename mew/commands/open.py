from rich import print

from mew.core.activator import (
    open_activated_shell
)

from mew.core.resolver import Resolver
from mew.registry import Registry
from mew.ui.select import select_environment


resolver = Resolver()
registry = Registry()


def run(name_or_id: str | None = None):

    environments = registry.get_all()

    if not environments:
        print("[yellow]No environments found[/yellow]")
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
            print("[red]Environment not found[/red]")
            return

        if len(matched) == 1:
            env = matched[0]

        else:
            env = select_environment(
                "Multiple environments found",
                matched
            )

    print(
        f"\n[green]Opening "
        f"{env.name} [{env.id}]...[/green]\n"
    )

    open_activated_shell(env)