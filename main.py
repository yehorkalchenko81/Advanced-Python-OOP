from classes import *


def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_birthday("24.03.2000")

    book.add_record(john_record)

    book.get_upcoming_birthdays()


if __name__ == '__main__':
    main()
