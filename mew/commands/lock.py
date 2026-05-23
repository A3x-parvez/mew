from rich import print

from mew.registry import Registry
from mew.core.resolver import Resolver
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

    # ------------------------
    # SELECT ENV
    # ------------------------

    if not name_or_id:

        env = select_environment(
            "Select environment to lock",
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
    # LOCK ENV
    # ------------------------

    env.locked = True

    registry.save(environments)

    print(
        f"\n[bold #00ff99]"
        f"Environment locked successfully"
        f"[/bold #00ff99]"
    )

    print(
        f"[bold #bb86fc]Name:[/bold #bb86fc] "
        f"{env.name}"
    )

    print(
        f"[bold #ff8800]ID:[/bold #ff8800] "
        f"{env.id}\n"
    )