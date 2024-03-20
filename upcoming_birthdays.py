from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> tuple:
    upcoming_birthdays, birthdays = [], []

    today = datetime.today()
    today_year_day = today.timetuple().tm_yday

    for user in users:
        name, date_of_birth = list(user.values())
        date_time_bd = datetime.strptime(date_of_birth, '%Y.%m.%d')
        birthday = datetime(year=today.year, month=date_time_bd.month, day=date_time_bd.day)
        birthday_year_day = birthday.timetuple().tm_yday

        if birthday.weekday() >= 5:
            birthday += timedelta(days=2) if birthday.weekday() == 5 else timedelta(days=1)

        if birthday_year_day - today_year_day in range(0, 7):
            upcoming_birthdays.append({
                'name': name,
                'congratulating_date': datetime.strftime(birthday, '%Y.%m.%d')
            })

        elif birthday_year_day - today_year_day > 7:
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

