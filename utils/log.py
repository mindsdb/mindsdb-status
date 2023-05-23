import logging


def setup_logger(logger_name, log_level=logging.DEBUG):
    """
    Set up a logger with the specified name and log level.

    :param logger_name: The name of the logger.
    :param log_level: The desired log level (default: logging.DEBUG).
    :return: The configured logger instance.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a stream handler and set the formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add the stream handler to the logger
    logger.addHandler(stream_handler)

    return logger
