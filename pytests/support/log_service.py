import logzero
from logzero import logger
log = logger


class LogService:

    # Método para logar qualquer INFO necessário no teste (evidência)
    def log_info(message):
        log_format = '[INFO %(asctime)s] %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        formatter = logzero.LogFormatter(fmt=log_format,datefmt=date_format)
        logzero.setup_default_logger(level='INFO', formatter=formatter)
        log.info(message)

    # Método para logar qualquer ERROR tratado necessário no teste (evidência)
    def log_error(message):
        log_format = '[ERROR %(asctime)s] %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        formatter = logzero.LogFormatter(fmt=log_format, datefmt=date_format)
        logzero.setup_default_logger(level='ERROR', formatter=formatter)
        log.error(message)
