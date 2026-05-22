import typer

from mew.commands import (
    craft,
    show,
    open,
    remove,
    about,
    close,
    sync
)

# Future shell integration
# from mew.shell.install import (
#     install,
#     uninstall
# )

# from mew.shell.init import (
#     shell_init
# )

app = typer.Typer(
    help="🐾 mew — Python environment manager"
)

# Future shell commands
# shell_app = typer.Typer(
#     help="Shell integration commands"
# )

# app.add_typer(
#     shell_app,
#     name="shell"
# )


# ------------------------
# ENV COMMANDS
# ------------------------

@app.command(name="craft")
def craft_env():
    craft.run()


@app.command(name="show")
def show_envs():
    show.run()


@app.command(name="open")
def open_env(
    name_or_id: str = typer.Argument(None)
):
    open.run(name_or_id)


@app.command(name="remove")
def remove_env(
    name_or_id: str = typer.Argument(None)
):
    remove.run(name_or_id)


@app.command(name="about")
def about_env(
    name_or_id: str = typer.Argument(None)
):
    about.run(name_or_id)


@app.command(name="close")
def close_env():
    close.run()


@app.command(name="sync")
def sync_envs():
    sync.run()


# ------------------------
# FUTURE SHELL COMMANDS
# ------------------------

# @shell_app.command(name="install")
# def shell_install():
#     install()


# @shell_app.command(name="uninstall")
# def shell_uninstall():
#     uninstall()


# ------------------------
# FUTURE INTERNAL INIT
# ------------------------

# @app.command(
#     name="init",
#     hidden=True
# )
# def init_shell(
#     shell: str
# ):
#     shell_init(shell)


# ------------------------

if __name__ == "__main__":
    app()