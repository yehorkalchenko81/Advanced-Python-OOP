from classes import AddressBook
from parsing import parse_input
from functions import command_add, command_change, command_phone, command_all, command_add_birthday


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(command_add(args, book))

        elif command == "change":
            print(command_change(args, book)) # Зробив шо потрібно вказувати старий номер так як він може бути не один

        elif command == "phone":
            print(command_phone(args, book))

        elif command == "all":
            print(command_all(book))

        elif command == "add-birthday":
            print(command_add_birthday())

        elif command == "show-birthday":
            pass

        elif command == "birthdays":
            pass

        else:
            print("Invalid command!")


if __name__ == '__main__':
    main()
