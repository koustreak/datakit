from h5py.h5r import OBJECT
from logging import *

def temp1(val):

    try:
        print(10/val)
        return 'a'
    except ZeroDivisionError as ex:
        raise Exception(ex)

x = temp1(10)
print(x)

import logging
import logging.handlers

# Create a custom logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level for this logger

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create file handler that logs debug and higher level messages
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)  # Set the level of the file handler
file_handler.setFormatter(formatter)  # Apply the formatter to the file handler

# Create a console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set the level of the console handler
console_handler.setFormatter(formatter)  # Apply the formatter to the console handler

# Create a rotating file handler that logs errors and above
rotating_file_handler = logging.handlers.RotatingFileHandler(
    'app_rotating.log', maxBytes=10000, backupCount=3)
rotating_file_handler.setLevel(logging.ERROR)  # Set the level of the rotating file handler
rotating_file_handler.setFormatter(formatter)  # Apply the formatter to the rotating file handler

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(rotating_file_handler)

def divide_numbers(a, b):
    logger.debug(f'Attempting to divide {a} by {b}')
    try:
        result = a / b
        logger.info(f'Result of division: {result}')
        return result
    except ZeroDivisionError as e:
        logger.error(f'Error occurred: {e}', exc_info=True)
        raise

def main():
    logger.info('Application started')

    try:
        divide_numbers(10, 2)
        divide_numbers(10, 0)  # This will raise an exception
    except Exception as e:
        logger.exception('Exception occurred during processing')

    logger.info('Application ended')

if __name__ == '__main__':
    main()
