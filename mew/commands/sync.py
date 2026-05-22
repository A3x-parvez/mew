from rich import print

from mew.core.scanner import Scanner


def run():

    print("\n[cyan]Syncing environments...[/cyan]\n")

    venvs = Scanner.sync_venvs()

    condas = Scanner.sync_conda()

    total = len(venvs) + len(condas)

    print(
        f"[green]✓ Synced "
        f"{total} environments[/green]"
    )