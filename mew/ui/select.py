from InquirerPy import inquirer


def select_choice(message: str, choices: list):

    return inquirer.select(
        message=message,
        choices=choices,
        cycle=True,
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
        message=message,
        choices=choices,
        cycle=True,
    ).execute()