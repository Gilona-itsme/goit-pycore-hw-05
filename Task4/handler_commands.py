import os
from decorators import input_error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "contacts.txt")

def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                name, phone = line.strip().split(":", 1)
                contacts[name.lower()]= phone
        return contacts
    except FileNotFoundError:
        return {}

@input_error 
def save_contacts(contacts):
    with open (FILE_NAME, "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name}: {phone}\n")


@input_error 
def add_contact(args, contacts):
    if len(args) != 2:
        return ValueError("Invalid input. Use: Add [name] [phone]")
    name, phone = args
    name = name.capitalize()
    contacts[name] = phone
    save_contacts(contacts)
    return (f"Contact '{name}' added.")

@input_error 
def change_contact(args, contacts):
    if len(args) != 2:
        return ValueError("Invalid input. Use: Change [name] [new_phone]")
    name, new_phone = args
    name = name.capitalize()
    if name in contacts:
        contacts[name]= new_phone
        save_contacts(contacts)
        return (f"contact '{name}' updated.")
    else:
        return KeyError(f"Contact '{name}' not found.")
@input_error
def show_phone_user(args, contacts):
    if len(args) != 1:
        return IndexError("Invalid input. Use: Phone [name]")
    name = args[0].capitalize()
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return KeyError(f"Contact {name} not found.")

def show_all(contacts):
    if not contacts:
        return KeyError("No contacts found.")
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)



