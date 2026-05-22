import typer

from mew.commands import craft, show

app = typer.Typer(
    help="🐾 mew — Python environment manager"
)


@app.command()
def craft_env():
    craft.run()


@app.command()
def show_envs():
    show.run()


if __name__ == "__main__":
    app()