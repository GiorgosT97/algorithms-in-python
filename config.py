import logging

FORMAT = '[%(asctime)s | %(levelname)s | %(name)s]: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG,
                    datefmt="%Y-%m-%d %H:%M:%S")


def get_logger(module_name):
    """ Return a configured logger object. """
    LOGGER = logging.getLogger(f'app:{module_name}')
    logging.basicConfig(format=FORMAT, level=logging.DEBUG,
                        datefmt="%Y-%m-%d %H:%M:%S")

    return LOGGER
