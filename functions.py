from classes import Record
from decorators import input_error


@input_error
def command_add(args, book):
    if len(args) < 2:
        return 'Not enough values for this commad!'
    contact = Record(args[0])
    contact.add_phone(args[1])
    book.add_record(contact)
    return f'{args[0]}\'s contact has been added'
