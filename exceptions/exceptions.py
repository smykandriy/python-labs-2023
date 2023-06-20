class NegativeAttributeValue(ValueError):
    """
    Exception class for representing a negative attribute value.

    This exception is raised when an attribute value is expected to be non-negative,
    but a negative value is encountered.

    Attributes:
        value_name (str): The name of the attribute with the negative value.
    """

    def __init__(self, value_name):
        super().__init__(
            f"Invalid {value_name} value: {value_name} cannot be negative."
        )


class InvalidLoggerMode(ValueError):
    """
    Exception class for representing an invalid logger mode.

    This exception is raised when an invalid logger mode is specified.
    The logger mode must be either 'console' or 'file'.
    """

    def __init__(self):
        super().__init__("Invalid logging mode. Must be 'console' or 'file'.")
