from InquirerPy import inquirer


def text_input(message: str):
    return inquirer.text(message=message).execute()


def confirm(message: str):
    return inquirer.confirm(message=message).execute()