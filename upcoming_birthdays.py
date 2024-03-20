from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> tuple:
    upcoming_birthdays, birthdays = [], []

    today = datetime.today()

    for user in users:
        name, date_of_birth = list(user.values())
        date_time_bd = datetime.strptime(date_of_birth, '%Y.%m.%d')
        birthday = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day)

        if birthday.weekday() >= 5:
            birthday += timedelta(days=2) if birthday.weekday() == 5 else timedelta(days=1)

        if birthday.timetuple().tm_yday - today.timetuple().tm_yday in range(0, 7):
            upcoming_birthdays.append({
                'name': name,
                'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')
            })

        elif birthday.timetuple().tm_yday - today.timetuple().tm_yday > 7:
            birthdays.append({
                'name': name,
                'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')
            })

        else:
            birthdays.append({
                'name': name,
                'congratulating_date': datetime.strftime(birthday.replace(year=birthday.year + 1), '%Y.%m.%d')
            })

    return upcoming_birthdays, birthdays

