import argparse
import logging

from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='log.log', filemode='w',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', ['name', 'extensions', 'dir', 'parent'])


def read_dir(dir_path: Path) -> None:
    if not dir_path.is_dir():
        raise ValueError(f'{dir_path} не является каталогом')
    if not dir_path.exists():
        raise FileNotFoundError(f'{dir_path} не найден')
    for file in dir_path.iterdir():
        obj = File(
            file.stem if file.is_file() else file.name,
            file.suffix,
            file.is_dir(),
            file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(Path(obj.parent)/obj.name)


def parse():
    parser = argparse.ArgumentParser(
        description='Получаем сожержимое каталога и сохраняем в файл логирования',
        prog='read_dir')
    parser.add_argument('-p', '--path', type=Path, required=True,
                        help='Путь к каталогу')
    args = parser.parse_args()
    try:
        read_dir(args.path)
        print(f'Информация о каталоге {args.path} записана в файл')
    except (ValueError, FileNotFoundError) as e:
        print(e)


if __name__ == '__main__':
    parse()
