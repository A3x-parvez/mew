from rich.console import Console
from rich.table import Table

console = Console()


def show_envs(environments):
    table = Table(title="🐾 Your Environments")

    table.add_column("Name")
    table.add_column("ID")
    table.add_column("Backend")
    table.add_column("Python")

    for env in environments:
        table.add_row(
            env.name,
            env.id,
            env.backend,
            env.python_version
        )

    console.print(table)