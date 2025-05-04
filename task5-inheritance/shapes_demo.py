# shapes_demo.py

from shapes import Circle, Rectangle, Triangle

def main():
    # Create a circle with radius 5
    circle = Circle(5, "green")
    print(circle)
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}\n")

    # Create a rectangle (width 4, height 6)
    rectangle = Rectangle(4, 6, "yellow")
    print(rectangle)
    print(f"Area: {rectangle.area():.2f}")
    print(f"Perimeter: {rectangle.perimeter():.2f}\n")

    # Create a square using class method
    square = Rectangle.square(4, "blue")
    print(square)
    print(f"Area: {square.area():.2f}")
    print(f"Perimeter: {square.perimeter():.2f}\n")

    # Create a triangle (3, 4, 5)
    triangle = Triangle(3, 4, 5, "red")
    print(triangle)
    print(f"Area: {triangle.area():.2f}")
    print(f"Perimeter: {triangle.perimeter():.2f}")

if __name__ == "__main__":
    main()
