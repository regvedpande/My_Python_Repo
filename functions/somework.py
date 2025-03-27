def calculate_area(shape, **kwargs):
    """
    Calculates the area of different shapes.

    Args:
        shape (str): The shape to calculate the area for (e.g., "circle", "rectangle", "triangle").
        **kwargs: Keyword arguments representing the dimensions of the shape.

    Returns:
        float: The calculated area, or None if the shape is invalid or dimensions are missing.
    """

    if shape == "circle":
        radius = kwargs.get("radius")
        if radius is not None:
            return 3.14159 * radius**2
        else:
            return None

    elif shape == "rectangle":
        length = kwargs.get("length")
        width = kwargs.get("width")
        if length is not None and width is not None:
            return length * width
        else:
            return None

    elif shape == "triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")
        if base is not None and height is not None:
            return 0.5 * base * height
        else:
            return None

    else:
        return None  # Invalid shape

# Example Usage
circle_area = calculate_area(shape="circle", radius=5)
rectangle_area = calculate_area(shape="rectangle", length=10, width=5)
triangle_area = calculate_area(shape="triangle", base=6, height=8)
invalid_area = calculate_area(shape="square", side = 5) #testing invalid shape.
missing_dimension = calculate_area(shape="rectangle", length = 10) #testing missing dimension

print(f"Circle Area: {circle_area}")
print(f"Rectangle Area: {rectangle_area}")
print(f"Triangle Area: {triangle_area}")
print(f"Invalid Area: {invalid_area}")
print(f"Missing Dimension: {missing_dimension}")
