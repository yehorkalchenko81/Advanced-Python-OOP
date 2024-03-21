from classes import Record, Phone
from decorators import input_error
from upcoming_birthdays import get_upcoming_birthdays

NOT_ENOUGH_VAL_MESSAGE = 'Not enough values for this commad!'
NOT_FOUND_CONT_MESSAGE = 'Contact has not been found!'


@input_error
def command_add(args, book):
    if len(args) < 2:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: add [name] [phone]'
    
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
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: change [name] [old-phone] [new-phone]'
    
    name, old_phone, phone, *_ = args

    if name not in book:
        return NOT_FOUND_CONT_MESSAGE
    
    contact = book.find(name)
    contact.edit_phone(old_phone, phone)

    return f'{args[0]}\'s contact has been changed!'


@input_error
def command_phone(args, book):
    if len(args) < 1:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: phone [name]'
    
    name, *_ = args

    if name not in book:
        return NOT_FOUND_CONT_MESSAGE
    
    contact = book.find(name)

    return f'{name}\'s phones:\n\t' + '\n\t'.join(contact.phones)


@input_error
def command_all(book):
    return 'All Contacts:\n\t' + '\n\t'.join(book.keys())


@input_error
def command_add_birthday(args, book):
    if len(args) < 2:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: add-birthday [name] [date-of-birth(DD.MM.YYYY)]'
    
    name, date_of_birth, *_ = args

    if name not in book:
        return NOT_FOUND_CONT_MESSAGE
    
    contact = book.find(name)
    contact.add_birthday(date_of_birth)

    return f'{name}\'s birth day has been updated!'



@input_error
def command_show_birthday(args, book):
    if len(args) < 1:
        return f'{NOT_ENOUGH_VAL_MESSAGE}\nSyntax: show-birthday [name]'
    
    name, *_ = args

    if name not in book:
        return NOT_FOUND_CONT_MESSAGE
    
    contact = book.find(name)
    birthday = contact.birthday

    if birthday:
        return f'{name}\'s birthday - {birthday.strftime('%d.%m.%Y')}'
    else:
        return f'{name}\'s birthday has not been found!'
    

@input_error
def birthdays(book):
    birthday_list = [{'name': name, 'congratulating_date': book.find(name).birthday} for name in book]

    return 'Upcoming birthdays:\n\t' + '\n\t'.join([f'{dc['name']}: {dc['congratulating_date']}' for dc in get_upcoming_birthdays(birthday_list)])
