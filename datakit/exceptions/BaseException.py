class BaseException(Exception):
    def __init__(self, message=None, code=None, context=None, *args):
        # Initialize the base class with the message and any extra arguments
        super().__init__(message, *args)

        # Store custom attributes
        self.message = message
        self.code = code
        self.context = context
        self.extra_info = args  # Store extra positional arguments

    def __str__(self):
        # Generate a string representation of the exception
        base_message = super().__str__()
        if self.code is not None:
            base_message += f" (Error Code: {self.code})"
        if self.context is not None:
            base_message += f" [Context: {self.context}]"
        if self.extra_info:
            base_message += f" [Extra Info: {', '.join(map(str, self.extra_info))}]"
        return base_message

    def get_extra_info(self):
        # Method to return extra information
        return self.extra_info


# Example usage
try:
    raise BaseException("An error occurred", 404, "File not found", "extra_detail1", "extra_detail2")
except BaseException as e:
    print(
        e)  # Output: An error occurred (Error Code: 404) [Context: File not found] [Extra Info: extra_detail1, extra_detail2]
    print("Extra Info:", e.get_extra_info())  # Output: Extra Info: ('extra_detail1', 'extra_detail2')
