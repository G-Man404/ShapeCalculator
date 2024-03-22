# Shape Calculator #

## What is this? ##
The Shape Calculator is a Python class designed to simplify geometric calculations such as calculating the area of a circle and a triangle, as well as checking if a triangle is right-angled.

## Quick Guide ##
The class provides methods for calculating the area of geometric shapes and checking the properties of triangles.

### Using ###
Using the Shape Calculator class is straightforward:

First, import the class:

```python
from shape_calculator import ShapeCalculator
```

Here are examples of operations available:

- Calculating the area of a circle with a given radius:

```python
circle_area = ShapeCalculator.get_area(5)
```

- Calculating the area of a triangle with given side lengths:

```python
triangle_area = ShapeCalculator.get_area(3, 4, 5)
```

- Checking if a triangle is right-angled:

```python
is_right_triangle = ShapeCalculator.is_right_triangle(3, 4, 5)
```

You can also directly use the methods `get_triangle_area()` and `get_circle_area()`:

- Calculating the area of a circle:

```python
circle_area = ShapeCalculator.get_circle_area(5)
```

- Calculating the area of a triangle:

```python
triangle_area = ShapeCalculator.get_triangle_area(3, 4, 5)
```

## Developer ##
For more information, visit my GitHub: [link](https://github.com/G-Man404/)