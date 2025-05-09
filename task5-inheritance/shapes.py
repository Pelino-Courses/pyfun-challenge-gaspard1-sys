# shapes.py

from abc import ABC, abstractmethod
import math

class Shape(ABC):


    def __init__(self, color: str = "Black"):
        """
        Args:
            color (str): The color of the shape.
        """
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.

        Returns:
            float: Area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.

        Returns:
            float: Perimeter of the shape.
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the shape.

        Returns:
            str: Description of the shape.
        """
        return f"A {self.color} {self.__class__.__name__}"


class Circle(Shape):
    """
    Circle shape class.
    """

    def __init__(self, radius: float, color: str = "Black"):
        """
        Initialize a Circle.

        Args:
            radius (float): Radius of the circle.
            color (str): Color of the circle.

        Raises:
            ValueError: If radius is not positive.
        """
        super().__init__(color)
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    @classmethod
    def from_diameter(cls, diameter: float, color: str = "Black"):
        """
        Create a Circle instance from diameter.

        Args:
            diameter (float): Diameter of the circle.
            color (str): Color of the circle.

        Returns:
            Circle: New Circle instance.
        """
        return cls(diameter / 2, color)

    def __str__(self) -> str:
        return f"{super().__str__()} with radius {self.radius}"


class Rectangle(Shape):
    """
    Rectangle shape class.
    """

    def __init__(self, w: float, h: float, color: str = "Black"):
        """
        Initialize a Rectangle.

        Args:
            w (float): Width of the rectangle.
            h (float): Height of the rectangle.
            color (str): Color of the rectangle.

        Raises:
            ValueError: If width or height is not positive.
        """
        super().__init__(color)
        if w <= 0 or h <= 0:
            raise ValueError("Width and height must be positive.")
        self.w = w
        self.h = h

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.w * self.h

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.w + self.h)

    @classmethod
    def square(cls, side_length: float, color: str = "Black"):
        """
        Create a Rectangle instance representing a square.

        Args:
            side_length (float): Length of each side.
            color (str): Color of the square.

        Returns:
            Rectangle: New Rectangle instance.
        """
        return cls(side_length, side_length, color)

    def __str__(self) -> str:
        return f"{super().__str__()} with width {self.w} and height {self.h}"


class Triangle(Shape):
    """
    Triangle shape class.
    """

    def __init__(self, a: float, b: float, c: float, color: str = "Black"):
        """
        Initialize a Triangle.

        Args:
            a (float): Length of side A.
            b (float): Length of side B.
            c (float): Length of side C.
            color (str): Color of the triangle.

        Raises:
            ValueError: If sides do not form a valid triangle.
        """
        super().__init__(color)
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Invalid side lengths for a triangle.")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _is_valid_triangle(x: float, y: float, z: float) -> bool:
        """Check if three sides can form a valid triangle."""
        return x + y > z and x + y > z and x + y > z

    def area(self) -> float:
        """print  the area of the triangle using Heron's formula."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """print the perimeter of the triangle."""
        return self.a + self.b + self.c

    def __str__(self) -> str:
        return (f"{super().__str__()} with sides "
                f"{self.a}, {self.b}, {self.c}")
