import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formater = logging.Formatter(
    '{levelname:<8} - {asctime}: {msg}', style='{')


class DebugFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        super().__init__(filename, mode, encoding, delay)

    def emit(self, record):
        if not (record.levelno == logging.DEBUG or record.levelno == logging.INFO):
            return
        super().emit(record)


logger_debag = DebugFileHandler('debug_info.log', encoding='utf-8')
logger_debag.setLevel(logging.DEBUG)
logger_debag.setFormatter(formater)
logger.addHandler(logger_debag)

logger_warning = logging.FileHandler('warnings_errors.log', encoding='utf-8')
logger_warning.setLevel(logging.WARNING)
logger_warning.setFormatter(formater)
logger.addHandler(logger_warning)

logger.debug(
    'Уровень DEBUG: Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Уровень INFO: Немного информации о работе кода')
logger.warning('Уровень WARNING: Внимание! Надвигается буря!')
logger.error('Уровень ERROR: Поймали ошибку. Дальше только неизвестность')
logger.critical('Уровень CRITICAL: На этом всё')
