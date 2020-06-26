import logging
import warnings
import os
from datetime import date


def setup_logger():
    warnings.filterwarnings('ignore')
    os.makedirs('logs', exist_ok=True)
    log_file = f'logs/app.{date.today().isoformat()}.log'
    log_level = logging.INFO
    log_fmt = '[%(asctime)s] %(levelname)s (%(module)s.%(funcName)s.%(lineno)d) :: %(message)s'
    logging.basicConfig(filename=log_file, level=log_level, format=log_fmt)


def format_info():
    pass


def format_error():
    pass
