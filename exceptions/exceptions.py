class NegativeAttributeValue(ValueError):
    """
    Exception class for representing a negative attribute value.

    This exception is raised when an attribute value is expected to be non-negative,
    but a negative value is encountered.

    Attributes:
        value_name (str): The name of the attribute with the negative value.
    """

    def __init__(self, value_name):
        self.value_name = value_name

    def __str__(self):
        return f"Invalid {self.value_name} value: {self.value_name} cannot be negative."


class InvalidLoggerMode(ValueError):
    def __str__(self):
        return "Invalid logging mode. Must be 'console' or 'file'."
