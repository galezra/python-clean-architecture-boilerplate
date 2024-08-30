"""
Data Transfer Objects (DTOs) for the application.

This module contains the DTO classes used for transferring data between different layers
of the application, such as between the API and use cases.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class BaseDTO(Generic[T]):
    """
    Base class for all DTOs in the application.

    This class provides a foundation for creating type-safe DTOs with common
    functionality.
    """

    def __init__(self, data: T) -> None:
        self.data: T = data

    def to_dict(self) -> dict:
        """
        Convert the DTO to a dictionary representation.

        This method should be overridden by subclasses to provide custom dictionary
        conversion logic if needed.
        """
        return vars(self)

    @classmethod
    def from_dict(cls, data: dict) -> "BaseDTO[T]":
        """
        Create a DTO instance from a dictionary.

        This method should be overridden by subclasses to provide custom instantiation
        logic from a dictionary if needed.
        """
        return cls(**data)
