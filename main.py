#!/usr/bin/env python3
"""
Main entry point for the actions-ex application.

This file serves as the primary entry point when running the application.
"""

import sys
from actions_ex.core import ExampleClass


def main():
    """Main function that runs the application."""
    print("Welcome to actions-ex!")
    print("=" * 30)

    # Create an example instance
    example = ExampleClass("Hello, World!")

    # Demonstrate the functionality
    print(f"Message: {example.message}")
    print(f"Reversed: {example.reverse_message()}")
    print(f"Length: {example.get_message_length()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

