from InquirerPy import inquirer


def select_choice(message: str, choices: list):
    return inquirer.select(
        message=message,
        choices=choices,
    ).execute()