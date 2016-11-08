import logging


def get_logger(name, verbose=None):
    """Custom logging"""
    logger = logging.getLogger(name)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s "
                                  "[%(name)s.%(funcName)s:%(lineno)d] %(message)s")
    handler.setFormatter(formatter)
    logger.handlers[:] = [handler]

    if verbose is True:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    return logger
