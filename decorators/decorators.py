import logging
import os
from datetime import datetime
from functools import wraps
from typing import Type

from exceptions.exceptions import InvalidLoggerMode


def validate_method_naming_convention(func):
    """
    Decorator that validates the naming convention of a method.

    The method name should follow the snake_case convention, i.e., all lowercase
    with words separated by underscores.

    Args:
        func (callable): The function or method to be decorated.

    Returns:
        callable: The decorated function or method.

    Raises:
        ValueError: If the method name does not follow the snake_case convention.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        method_name = func.__name__
        if not method_name.islower() or "_" not in method_name:
            raise ValueError("Method name should follow snake_case convention")
        return func(self, *args, **kwargs)

    return wrapper


def log_method_calls(filename):
    """
    Decorator that logs the method calls to a file.

    The decorator appends the method name and the timestamp of the method call
    to the specified log file.

    Args:
        filename (str): The name of the log file.

    Returns:
        callable: The decorator.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            directory = "logs/"
            os.makedirs(directory, exist_ok=True)
            file_path = os.path.join(directory, filename)
            with open(file_path, "a") as file:
                timestamp = datetime.now()
                log_message = f"Method '{func.__name__}' called at {timestamp}\n"
                file.write(log_message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def logged(exception: Type[Exception], mode):
    """
    Decorator that logs exceptions using the logging module.

    The decorator logs the exceptions raised in the decorated method using the
    specified mode: "console" or "file". In "console" mode, the exceptions are logged
    to the console. In "file" mode, the exceptions are logged to a file.

    Args:
        exception (Exception): The exception class to be logged.
        mode (str): The mode of logging: "console" or "file".

    Returns:
        callable: The decorator.

    Raises:
        ValueError: If an invalid mode is specified.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode.lower() == "console":
                    raise e
                elif mode.lower() == "file":
                    log_file = "logs/exceptions.log"
                    os.makedirs(os.path.dirname(log_file), exist_ok=True)
                    logging.basicConfig(filename=log_file, level=logging.ERROR)
                    logging.exception(e)
                else:
                    raise InvalidLoggerMode

        return wrapper

    return decorator
