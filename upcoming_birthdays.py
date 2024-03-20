from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> tuple:
    upcoming_birthdays, birthdays = [], []

    today = datetime.today()

    for user in users:
        name, date_of_birth = list(user.values())
        date_time_bd = datetime.strptime(date_of_birth, '%Y.%m.%d')
        birthday = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day)
        res = birthday.timetuple().tm_yday - today.timetuple().tm_yday

        if birthday.weekday() >= 5:
            birthday += timedelta(days=7-birthday.weekday())

        if res in range(0, 7):
            upcoming_birthdays.append({
                'name': name,
                'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')
            })
            
        else:
            birthdays.append({
                'name': name,
                'congratulating_date': datetime.strftime(birthday.replace(year=birthday.year + 0 if res > 7 else birthday.year + 1), '%Y.%m.%d')
            })

    return upcoming_birthdays, birthdays
    