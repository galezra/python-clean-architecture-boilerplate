"""
Entities package for defining base and derived entity classes.
"""

from abc import ABCMeta, abstractmethod
from typing import Any, Optional, TypeVar

from pydantic.dataclasses import dataclass

T = TypeVar("T", bound="BaseEntity")


@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: Optional[int]

    @classmethod
    @abstractmethod
    def from_dict(cls: type[T], other: dict[str, Any]) -> T:
        """
        Create an instance of the entity from a dictionary.
        """

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert the entity to a dictionary.
        """
