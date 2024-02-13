import logging


def get_logger(name: str, path: str = None, stream: bool = False):
    logger = logging.getLogger(name=name)
    logger.propagate = False
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(funcName)s(%(lineno)d) %(message)s',
                                  datefmt='%d/%m/%Y %H:%M:%S')

    if len(logger.handlers) == 0:  # this is for preventing adding multiple handlers when calling get_logger()
        if stream:
            sh = logging.StreamHandler()
            sh.setFormatter(formatter)
            sh.setLevel(logging.INFO)
            logger.addHandler(sh)
        if path is not None:
            fh = logging.FileHandler(path)
            fh.setFormatter(formatter)
            fh.setLevel(logging.INFO)
            logger.addHandler(fh)

    return logger
