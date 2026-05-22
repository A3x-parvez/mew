from InquirerPy import inquirer
from InquirerPy import get_style


STYLE = get_style(
    {
        "questionmark": "#ff006e bold",
        "question": "#bb86fc bold",
        "answer": "#00ff99 bold",
        "pointer": "#ff8800 bold",
        "highlighted": "#ff8800 bold",
        "selected": "#00ff99 bold",
        "separator": "#666666",
        "instruction": "#ffb703 italic",
        "text": "#ffffff",
    }
)


def select_choice(message: str, choices: list):

    return inquirer.select(
        message=f" {message}",
        choices=choices,
        cycle=True,
        pointer="❯",
        instruction="↑ ↓ navigate • enter select",
        qmark="●",
        amark="✓",
        border=False,
        style=STYLE,
        height=min(len(choices) + 2, 10),
    ).execute()


def select_environment(message: str, environments: list):

    choices = [
        {
            "name": (
                f"{env.name} "
                f"[{env.id}] "
                f"({env.backend})"
            ),
            "value": env
        }
        for env in environments
    ]

    return inquirer.select(
        message=f" {message}",
        choices=choices,
        cycle=True,
        pointer="❯",
        instruction="↑ ↓ navigate • enter select",
        qmark="●",
        amark="✓",
        border=False,
        style=STYLE,
        height=min(len(choices) + 2, 10),
    ).execute()