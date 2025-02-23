import argparse


def info() -> None:
    parser = argparse.ArgumentParser(
        description='Скрипт работает с аргументами командной строки')
    parser.add_argument('-n', '--number', type=int,
                        required=True, help='Число для вывода')
    parser.add_argument('-t', '--text', type=str,
                        required=True, help='Строка для вывода')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Вывод дополнтьельной информации')
    parser.add_argument('-r', '--repeat', type=int, default=1,
                        help='Количество повторенйи строки вывода')

    args = parser.parse_args()
    if args.verbose:
        print(
            f'Дополнительная информация: number={args.number}, text={args.text}, repeat={args.repeat}')
    print(f'Число number={args.number}, текст text={args.text*args.repeat}')


if __name__ == '__main__':
    info()
