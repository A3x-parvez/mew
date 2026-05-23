from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.columns import Columns
from rich.text import Text
from rich.rule import Rule
from rich.padding import Padding
from rich import box


console = Console()


PURPLE = "#bb86fc"
GREEN  = "#00ff99"
CYAN   = "#00d4ff"
ORANGE = "#ff8800"
RED    = "#ff4444"
DIM    = "grey50"


mew_logo = (
    """

"""
)

_PAW_BRAILLE = (
"""                      
⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣷⠀⠀⢠⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⣸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀
⠀⣠⣶⣦⡀⠹⣿⣿⣿⣿⡿⠁⠀⠘⣿⣿⣿⣿⣿⠇⣠⣴⣶⡄⠀
⢰⣿⣿⣿⣿⣆⠉⠛⠛⠋⠁⣀⣀⣀⠈⠛⠛⠛⠁⣼⣿⣿⣿⣿⡀
⢸⣿⣿⣿⣿⣿⡆⠀⢀⣴⣿⣿⣿⣿⣿⣦⠀⠀⢸⣿⣿⣿⣿⣿⡇
⠈⢿⣿⣿⣿⣿⠃⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢸⣿⣿⣿⣿⠟⠀
⠀⠀⠉⠙⠋⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣍⠛⠋⠁⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀"""
)


# def _header() -> Panel:
#     t = Text(justify="left")

#     # Paw logo
#     t.append(_PAW_BRAILLE, style=f"bold {PURPLE}")
#     t.append("\n")

#     left = Text(justify="left")
#     left.append(_PAW_BRAILLE, style=f"bold {PURPLE}")

#     right = Text(justify="left")
#     right.append("\n\n")
#     right.append("mew\n", style=f"bold {PURPLE}")
#     right.append("Cute Python Environment Manager\n", style=f"bold {GREEN}")
#     right.append("\n")
#     right.append("Developer: ", style=f"bold {CYAN}")
#     right.append("parvez\n", style="white")
#     right.append("Version:   ", style=f"bold {ORANGE}")
#     right.append("0.1.0",   style="white")

#     combined = Columns([left, right], expand=False, equal=False)

#     return Panel(
#         combined,
#         border_style=PURPLE,
#         box=box.DOUBLE_EDGE,
#         padding=(0, 2),
#     )

# def _header() -> Panel:

#     left = Text(justify="center")

#     left.append(
#         "⠀⠀⠀⠀⣀⡀\n"
#         "⢠⣤⡀⣾⣿⣿⠀⣤⣤⡄\n"
#         "⢿⣿⡇⠘⠛⠁⢸⣿⣿⠃\n"
#         "⠈⣉⣤⣾⣿⣿⡆⠉⣴⣶⣶\n"
#         "⣾⣿⣿⣿⣿⣿⣿⡀⠻⠟⠃\n"
#         "⠙⠛⠻⢿⣿⣿⣿⡇\n"
#         "⠀⠀⠀⠀⠈⠙⠋⠁",
#         style=f"bold {PURPLE}"
#     )

#     right = Text(justify="left")

#     right.append("\n")

#     right.append(
#         "mew\n",
#         style=f"bold {PURPLE}"
#     )

#     right.append(
#         "Cute Python Environment Manager\n\n",
#         style=f"bold {GREEN}"
#     )

#     right.append(
#         "Developer: ",
#         style=f"bold {CYAN}"
#     )

#     right.append(
#         "parvez\n",
#         style="white"
#     )

#     right.append(
#         "Version: ",
#         style=f"bold {ORANGE}"
#     )

#     right.append(
#         "0.1.0",
#         style="white"
#     )

#     content = Columns(
#         [left, right],
#         equal=False,
#         expand=True,
#     )

#     return Panel(
#         content,
#         border_style=PURPLE,
#         box=box.DOUBLE_EDGE,
#         padding=(1, 3),
#     )


def _header() -> Panel:

    left = Text(justify="center")

    left.append(
        "⠀⠀⠀⠀⣀⡀\n"
        "⢠⣤⡀⣾⣿⣿⠀⣤⣤⡄\n"
        "⢿⣿⡇⠘⠛⠁⢸⣿⣿⠃\n"
        "⠈⣉⣤⣾⣿⣿⡆⠉⣴⣶⣶\n"
        "⣾⣿⣿⣿⣿⣿⣿⡀⠻⠟⠃\n"
        "⠙⠛⠻⢿⣿⣿⣿⡇\n"
        "⠀⠀⠀⠀⠈⠙⠋⠁",
        style=f"bold {PURPLE}"
    )

    right = Text(justify="left")

    right.append("\n")

    # BIG TITLE
    right.append(
        "███╗   ███╗███████╗██╗    ██╗",
        style=f"bold {PURPLE}"
    )

    right.append(
        "        ",
        style="white"
    )

    right.append(
        "Developer : ",
        style=f"bold {CYAN}"
    )

    right.append(
        "A3x-parvez\n",
        style="white"
    )

    right.append(
        "████╗ ████║██╔════╝██║    ██║",
        style=f"bold {PURPLE}"
    )

    right.append(
        "        ",
        style="white"
    )

    right.append(
        "Version   : ",
        style=f"bold {ORANGE}"
    )

    right.append(
        "0.1.0\n",
        style="white"
    )

    right.append(
        "██╔████╔██║█████╗  ██║ █╗ ██║",
        style=f"bold {PURPLE}"
    )

    right.append(
        "        ",
        style="white"
    )

    right.append(
        "Shells    : ",
        style=f"bold {CYAN}"
    )

    right.append(
        "PowerShell • CMD • Bash\n",
        style="white"
    )

    right.append(
        "██║╚██╔╝██║██╔══╝  ██║███╗██║",
        style=f"bold {PURPLE}"
    )

    right.append(
        "        ",
        style="white"
    )

    right.append(
        "Supports  : ",
        style=f"bold {ORANGE}"
    )

    right.append(
        "venv • Conda\n",
        style="white"
    )

    right.append(
        "██║ ╚═╝ ██║███████╗╚███╔███╔╝",
        style=f"bold {PURPLE}"
    )

    right.append(
        "        ",
        style="white"
    )

    right.append(
        "Platform  : ",
        style=f"bold {GREEN}"
    )

    right.append(
        "Windows • Linux • macOS\n",
        style="white"
    )

    right.append(
        "╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝\n\n",
        style=f"bold {PURPLE}"
    )

    right.append(
        "Cute Python Environment Manager      Manage your virtual environments with ease and style.",
        style=f"bold {GREEN}"
    )

    content = Columns(
        [left, right],
        equal=False,
        expand=True,
    )

    return Panel(
        content,
        border_style=PURPLE,
        box=box.DOUBLE_EDGE,
        padding=(1, 4),
    )

def _paw_title(label: str) -> Text:
    t = Text(justify="center")
    t.append("  ", style=f"{PURPLE}")
    t.append(f" {label} ", style=f"bold {PURPLE}")
    t.append("  ", style=f"{PURPLE}")
    return t


def _commands_table() -> Table:
    tbl = Table(
        title=_paw_title("Available Commands"),
        border_style=PURPLE,
        header_style=f"bold {CYAN}",
        box=box.SIMPLE_HEAD,
        expand=True,
        show_edge=True,
        padding=(0, 1),
    )

    tbl.add_column("Command",  style=f"bold {GREEN}",  no_wrap=True)
    tbl.add_column("Purpose",  style=f"{ORANGE}")
    tbl.add_column("Example",  style=f"dim {PURPLE}",  no_wrap=True)

    rows = [
        ("mew craft",        "Create environment",           "mew craft"),
        ("mew open",         "Open environment selector",    "mew open"),
        ("mew open <name>",  "Open using environment name",  "mew open api"),
        ("mew open <id>",    "Open using environment ID",    "mew open 8ee0d6"),
        ("mew close",        "Deactivate current environment","mew close"),
        ("mew show",         "List all environments",        "mew show"),
        ("mew about",        "Detailed environment info",    "mew about"),
        ("mew remove",       "Delete environment",           "mew remove"),
        ("mew clone",        "Clone environment",            "mew clone"),
        ("mew sync",         "Sync existing environments",   "mew sync"),
        ("mew lock",         "Protect environment",          "mew lock"),
        ("mew unlock",       "Remove protection",            "mew unlock"),
    ]

    for cmd, purpose, example in rows:
        tbl.add_row(cmd, purpose, example)

    # return tbl

    return Panel(
        tbl,
        border_style=PURPLE,
        box=box.DOUBLE_EDGE,
        padding=(0, 1),
        expand=True,
    )


def _tips_panel() -> Panel:
    tips = [
        [("• ", PURPLE), ("Use both ", "white"), ("name", GREEN),
         (" and ", "white"), ("ID", ORANGE), (" for most commands.", "white")],

        [("• ", PURPLE), ("Locked", RED),
         (" environments cannot be removed.", "white")],

        [("• ", PURPLE), ("Supports both ", "white"), ("venv", GREEN),
         (" and ", "white"), ("Conda", PURPLE), (".", "white")],

        [("• ", PURPLE), ("Interactive selector with arrow key navigation.", "white")],

        [("• ", PURPLE), ("Detects ", "white"), ("PowerShell", CYAN),
         (", ", "white"), ("CMD", ORANGE), (", and ", "white"),
         ("Bash", GREEN), (" automatically.", "white")],

        [("• ", PURPLE), ("Registry tracks all your environments.", "white")],

        [("• ", PURPLE), ("Clone duplicates an existing environment.", "white")],

        [("• ", PURPLE), ("Sync keeps envs consistent across machines.", "white")],
    ]

    title = Text(justify="center")
    title.append("  ", style=PURPLE)
    title.append(" mew ", style=f"bold {GREEN}")
    title.append("Tips ", style=f"bold {PURPLE}")
    title.append("  ", style=PURPLE)
    title.append("\n")

    body = Text()
    body.append_text(title)

    for i, segments in enumerate(tips):
        if i > 0:
            body.append("\n")
            body.append("─" * 32 + "\n", style=f"dim {PURPLE}")
        tip_line = Text()
        for text, color in segments:
            tip_line.append(text, style=color)
        body.append_text(tip_line)

    return Panel(
        body,
        border_style=PURPLE,
        box=box.DOUBLE_EDGE,
        padding=(0, 1),
        expand=True,
    )


def run() -> None:
    console.print()
    console.print(_header())
    console.print()
    console.print(
        Columns(
            [_commands_table(), _tips_panel()],
            equal=False,
            expand=True,
        )
    )
    console.print()


if __name__ == "__main__":
    run()