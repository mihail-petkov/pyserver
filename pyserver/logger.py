import logging

class Pylogger:

    logger = None

    @classmethod
    def init(cls, log_level=None):
        logging.basicConfig()
        cls.logger = logging.getLogger('pyserver')
        if log_level:
            cls.logger.setLevel(log_level)
        else:
            cls.logger.setLevel(logging.DEBUG)
