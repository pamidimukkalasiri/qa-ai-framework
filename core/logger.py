import logging
import sys
from cgitb import handler


def get_logger(name : str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
    return logger
#single logger instance used across framework
logger = get_logger("qa-framework")