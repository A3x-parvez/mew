from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


console = Console()



def show_envs(environments):


    table = Table(
        title="🐾 Your Environments",
        border_style="bright_magenta",
        header_style="bold cyan"
    )

    table.add_column(
        "Name",
        style="bold green"
    )

    table.add_column(
        "ID",
        style="bold yellow"
    )

    table.add_column(
        "Backend",
        style="bold magenta"
    )

    table.add_column(
        "Python",
        style="bold cyan"
    )

    for env in environments:

        backend_icon = (
            "🐍"
            if env.backend == "venv"
            else "🧪"
        )

        lock_icon = (
            "🔒"
            if getattr(env, "locked", False)
            else "🔓"
        )

        table.add_row(
            f"{lock_icon} {env.name}",
            env.id,
            f"{backend_icon} {env.backend}",
            env.python_version
        )

    console.print(table)


def show_info(message: str):

    console.print(
        f"\n[bold cyan]➜ {message}[/bold cyan]"
    )


def show_success(message: str):

    console.print(
        f"\n[bold green]✓ {message}[/bold green]"
    )


def show_error(message: str):

    console.print(
        f"\n[bold red]✗ {message}[/bold red]"
    )