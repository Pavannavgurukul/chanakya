import logging
import logging.handlers

class Loggly(object):
    @staticmethod
    def create_logger(traceback, log_level):
        logger = logging.getLogger('Chanakya')
        logger.setLevel(log_level)

        #add handler to the logger
        handler = logging.handlers.SysLogHandler('/dev/log')

        #add formatter to the handler
        formatter = logging.Formatter("""Chanakya: {
            "loggerName":"%(name)s",
            "timestamp":"%(asctime)s",
            "pathName":"%(pathname)s",
            "logRecordCreationTime":"%(created)f",
            "levelNo":"%(levelno)s",
            "lineNo":"%(lineno)d",
            "levelName":"%(levelname)s",
            "message":"%(message)s",
            "traceback":"%(traceback)s"
        }""")

        extra = {
            'traceback':''.join(traceback)
        }

        logger.addHandler(handler)
        handler.formatter = formatter
        logger = logging.LoggerAdapter(logger, extra)

        return logger

    @staticmethod
    def error(exception, traceback):
        """Log error level messages."""
        logger = Loggly.create_logger(traceback, logging.ERROR)
        logger.error(exception, exc_info=True)

    @staticmethod
    def warn(exception, traceback):
        """Log warning level messages."""

        logger = Loggly.create_logger(traceback, logging.WARN)
        logger.warn(exception, exc_info=True)


    @staticmethod
    def debug(exception, traceback):
        """Log debug level messages."""

        logger = Loggly.create_logger(traceback, logging.DEBUG)
        logger.debug(exception, exc_info=True)


    @staticmethod
    def critical(exception, traceback):
        """Log verbose level messages."""

        logger = Loggly.create_logger(traceback, logging.CRITICAL)
        logger.critical(exception, exc_info=True)
