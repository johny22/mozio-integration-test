import logging


def define_log_level(option):
    options = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO
    }
    return options.get(option, logging.DEBUG)
