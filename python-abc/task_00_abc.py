#!/usr/bin/env python3
"""Module defining abstract Animal class and its concrete subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a Dog."""

    def sound(self):
        """Returns the dog sound."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a Cat."""

    def sound(self):
        """Returns the cat sound."""
        return "Meow"
