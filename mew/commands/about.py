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
        console.print("[yellow]No environments found[/yellow]")
        return

    if not name_or_id:

        env = select_environment(
            "Select environment",
            environments
        )

    else:

        matched = resolver.resolve(name_or_id)

        if not matched:
            console.print("[red]Environment not found[/red]")
            return

        if len(matched) == 1:
            env = matched[0]

        else:
            env = select_environment(
                "Multiple environments found",
                matched
            )

    content = f"""
[bold cyan]Name:[/bold cyan] {env.name}
[bold cyan]ID:[/bold cyan] {env.id}
[bold cyan]Backend:[/bold cyan] {env.backend}
[bold cyan]Python:[/bold cyan] {env.python_version}
[bold cyan]Path:[/bold cyan] {env.path}
[bold cyan]Created:[/bold cyan] {env.created_at}
"""

    console.print(
        Panel.fit(
            content,
            title=f"🐾 {env.name}",
            border_style="cyan"
        )
    )