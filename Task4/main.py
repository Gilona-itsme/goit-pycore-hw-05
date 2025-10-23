from input_data import parse_input
from handler_commands import  load_contacts, add_contact, change_contact, show_phone_user, show_all

#Task4: Main script for assistant bot
#Added error handling with the help of decorators.


def main():
    contacts = load_contacts()
    print("Welcome to the assistant bot! Type 'Hello' to start or 'Close'/'Exit' to quit.")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye! See you later!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone_user(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main() 
