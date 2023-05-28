import os
from datetime import datetime


def validate_method_naming_convention(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        if not method_name.islower() or "_" not in method_name:
            raise ValueError("Method name should follow snake_case convention")
        return func(*args, **kwargs)

    return wrapper()


def log_method_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            directory = "methods_logs/"
            os.makedirs(directory, exist_ok=True)
            file_path = os.path.join(directory, filename)
            with open(file_path, "a") as file:
                timestamp = datetime.now()
                log_message = f"Method '{func.__name__}' called at {timestamp}\n"
                file.write(log_message)
            return func(*args, **kwargs)

        return wrapper

    return decorator
