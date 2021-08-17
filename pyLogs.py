import logging
from logging.handlers import RotatingFileHandler

if __name__ == "__main__":

    # Easy Way
    '''
        handlers = [logging.FileHandler("LogFileName.log"), logging.StreamHandler()]

        logging.basicConfig(
            format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO, datefmt='%c',handlers=handlers)
        logger = logging.getLogger(__name__)
    '''
    
    # Log file name
    logfile = 'LogSample.log'

    # Format to be used for logging
    formatter = logging.Formatter("[%(asctime)-8s] %(levelname)-8s : %(message)s")

    log = logging.getLogger()

    # Set the lowest logging level to be loged
    log.setLevel(logging.INFO)

    # Using Stream handler to print the logs on screen
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Log roration after 20MB total log file will be 5
    exp_file_handler = RotatingFileHandler(logfile, maxBytes=2000000, backupCount=5)
    exp_file_handler.setLevel(logging.INFO)
    exp_file_handler.setFormatter(formatter)

    # Adding both the handlers
    log.addHandler(console_handler)
    log.addHandler(exp_file_handler)

    # Examples
    log.debug("Log debugger is collecting logs")
    log.info("Log info is collected")
    log.warning("warning are collected")
    log.error("This is dangreous error")
    log.critical("This is not acceptable its crital")
