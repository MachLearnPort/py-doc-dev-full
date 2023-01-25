import logging

def configure_logger(log_file: str):
    """
    Configure the logger to log messages to a file
    """
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logger = logging.getLogger()
    return logger

