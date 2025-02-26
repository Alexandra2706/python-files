from datetime import datetime


def get_date() -> str:
    # переводит текущее время и дату в формат YYYY-MM-DD HH:MM:SS
    current_date = datetime.now()
    str_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = current_date.strftime('%A')
    week_in_year = current_date.strftime('%W')
    return f'Текущая дата и время: {str_date}. День недели: {day_of_week}. Номер недели в году: {week_in_year}'


if __name__ == '__main__':
    print(get_date())
