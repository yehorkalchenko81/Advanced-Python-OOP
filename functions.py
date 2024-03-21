from classes import Record, Phone
from decorators import input_error

NOT_ENOUGH_VAL_MESSAGE = 'Not enough values for this commad!'
NOT_FOUND_CONT_MESSAGE = 'Contact has not been found!'


@input_error
def command_add(args, book):
    if len(args) < 2:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: add name phone'
    
    name, phone, *_ = args

    if name in book:
        contact = book.find(name)
    else:
        contact = Record(name)

    contact.add_phone(phone)
    book.add_record(contact)

    return f'{args[0]}\'s contact has been added!'


@input_error
def command_change(args, book):
    if len(args) < 3:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: change name old_phone new_phone'
    
    name, old_phone, phone, *_ = args

    if name not in book:
        return NOT_FOUND_CONT_MESSAGE
    
    contact = book.find(name)
    contact.edit_phone(old_phone, phone)
    book.add_record(contact)

    return f'{args[0]}\'s contact has been changed!'


@input_error
def command_phone(args, book):
    if len(args) < 1:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: phone name'
    
    name, *_ = args

    if name not in book:
        return NOT_FOUND_CONT_MESSAGE
    
    contact = book.find(name)

    return contact.phones
