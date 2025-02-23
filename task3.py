from datetime import datetime, timedelta, date


def next_date(days: int) -> date:
    current_date = datetime.now()
    delta = timedelta(days=days)
    return (current_date + delta).strftime('%Y-%m-%d')


def get_days_form(days: int) -> date:
    remainder = days % 10
    if days == 0 or remainder == 0 or remainder >= 5 or days in range(11, 19):
        return 'дней'
    elif remainder == 1:
        return 'день'
    else:
        return 'дня'


if __name__ == '__main__':
    days = 1
    for days in range(0, 33):
        print(f'Через {days} {get_days_form(days)} наступит {next_date(days)}')
