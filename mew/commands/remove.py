from rich import print

from mew.core.resolver import Resolver
from mew.core.storage import Storage
from mew.registry import Registry
from mew.ui.prompt import confirm
from mew.ui.select import select_environment


registry = Registry()
resolver = Resolver()


def run(name_or_id: str | None = None):

    environments = registry.get_all()

    if not environments:
        print("[yellow]No environments found[/yellow]")
        return

    if not name_or_id:
        env = select_environment(
            "Select environment to remove",
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

    ok = confirm(
        f"Remove {env.name} [{env.id}]?"
    )

    if not ok:
        print("[yellow]Cancelled[/yellow]")
        return

    if env.backend == "venv":
        Storage.delete_env(env.path)

    registry.remove(env.id)

    print(f"[green]Removed {env.name} [{env.id}][/green]")