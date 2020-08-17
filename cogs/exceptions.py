
"""
Example Exception

class (Exception):
    ""Raised when ""

    def __init__(self, message=""):
        super().__init__(self.message)

    def __str__(self):
        return self.message
"""


class TagAlreadyExists(Exception):
    """Raised when the inputted tag already exists"""

    def __init__(self, message="The inputted tag already exists"):
        super().__init__(self.message)

    def __str__(self):
        return self.message
