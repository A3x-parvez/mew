from rich.console import Console
from rich.panel import Panel

from mew.core.resolver import Resolver
from mew.registry import Registry
from mew.ui.select import select_environment


console = Console()

registry = Registry()
resolver = Resolver()


def run(name_or_id: str | None = None):

    environments = registry.get_all()

    if not environments:

        console.print(
            "[bold #ff8800]"
            "No environments found"
            "[/bold #ff8800]"
        )

        return

    if not name_or_id:

        env = select_environment(
            "Select environment",
            environments
        )

    else:

        matched = resolver.resolve(name_or_id)

        if not matched:

            console.print(
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
    # STATUS ICONS
    # ------------------------

    backend_icon = (
        "🐍"
        if env.backend == "venv"
        else "🧪"
    )

    lock_status = (
        "[bold red]Locked 🔒[/bold red]"
        if getattr(env, "locked", False)
        else "[bold green]Unlocked 🔓[/bold green]"
    )

    # ------------------------
    # CONTENT
    # ------------------------

    content = f"""
[bold #bb86fc]Name:[/bold #bb86fc] {env.name}
[bold #ff8800]ID:[/bold #ff8800] {env.id}
[bold cyan]Backend:[/bold cyan] {backend_icon} {env.backend}
[bold green]Python:[/bold green] {env.python_version}
[bold magenta]Path:[/bold magenta] {env.path}
[bold yellow]Created:[/bold yellow] {env.created_at}
[bold cyan]Protection:[/bold cyan] {lock_status}
"""

    console.print(
        Panel.fit(
            content,
            title=f"🐾 {env.name}",
            border_style="bright_magenta"
        )
    )