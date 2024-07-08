import utils.constants


def change_phone_by_name(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        print(f"{name} phone number changed to {new_phone}.")
    else:
        print(f"{name} not found.")


def get_phone_by_name(args, contacts):
    name = args[0]
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found.")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    name = name.strip().capitalize()
    contacts[name] = phone
    return "Contact added."


def print_commands():
    print(utils.constants.COMMANDS)
