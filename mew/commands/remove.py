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

        print(
            "[bold #ff8800]"
            "No environments found"
            "[/bold #ff8800]"
        )

        return

    if not name_or_id:

        env = select_environment(
            "Select environment to remove",
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
    # LOCK CHECK
    # ------------------------

    if getattr(env, "locked", False):

        print(
            "\n[bold red]"
            "Environment is locked"
            "[/bold red]"
        )

        print(
            "[bold #ff8800]"
            "Unlock it before removal"
            "[/bold #ff8800]\n"
        )

        return

    # ------------------------
    # CONFIRM REMOVE
    # ------------------------

    ok = confirm(
        f"Remove {env.name} [{env.id}]?"
    )

    if not ok:

        print(
            "[bold yellow]"
            "Cancelled"
            "[/bold yellow]"
        )

        return

    # ------------------------
    # DELETE ENV
    # ------------------------

    if env.backend == "venv":

        Storage.delete_env(env.path)

    registry.remove(env.id)

    print(
        f"\n[bold #00ff99]"
        f"Removed {env.name} "
        f"[{env.id}]"
        f"[/bold #00ff99]\n"
    )