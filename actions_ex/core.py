"""
Core functionality for the actions-ex application.

This module contains the main business logic and classes.
"""


class ExampleClass:
    """
    An example class that demonstrates basic Python functionality.
    
    This class provides simple string manipulation methods as an example
    of how to structure your code.
    """

    def __init__(self, message: str):
        """
        Initialize the ExampleClass with a message.
        
        Args:
            message: The message to store and manipulate
        """
        self.message = message

    def reverse_message(self) -> str:
        """
        Reverse the stored message.
        
        Returns:
            The reversed message
        """
        return self.message[::-1]

    def get_message_length(self) -> int:
        """
        Get the length of the stored message.
        
        Returns:
            The length of the message
        """
        return len(self.message)

    def get_message_words(self) -> list[str]:
        """
        Split the message into words.
        
        Returns:
            List of words from the message
        """
        return self.message.split()

    def to_uppercase(self) -> str:
        """
        Convert the message to uppercase.
        
        Returns:
            The message in uppercase
        """
        return self.message.upper()

    def to_lowercase(self) -> str:
        """
        Convert the message to lowercase.
        
        Returns:
            The message in lowercase
        """
        return self.message.lower()

    def __str__(self) -> str:
        """String representation of the class."""
        return f"ExampleClass(message='{self.message}')"

    def __repr__(self) -> str:
        """Detailed string representation of the class."""
        return f"ExampleClass(message='{self.message}')"
