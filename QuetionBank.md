# Python Full Stack Development - Concepts

## 1. Difference between List and Tuple in Python

- **List**: Mutable (can be modified), defined with square brackets `[]`. Items can be added, removed, or modified.
- **Tuple**: Immutable (cannot be modified), defined with parentheses `()`. Items cannot be added, removed, or modified after creation.

## 2. Different Types of Function Arguments in Python

- **Positional arguments**: Passed by position (e.g., `def func(a, b)`).
- **Keyword arguments**: Passed by name (e.g., `def func(a, b)` can be called as `func(a=1, b=2)`).
- **Default arguments**: Arguments with default values (e.g., `def func(a, b=2)`).
- **Variable-length arguments**: `*args` for non-keyword variable arguments and `**kwargs` for keyword variable arguments.

## 3. Object-Oriented Programming (OOP) in Python

OOP is a paradigm where data and behaviors are encapsulated within classes and objects. It focuses on the following:

- **Classes**: Blueprints for creating objects.
- **Objects**: Instances of a class.
- **Encapsulation**: Bundling data and methods that operate on the data into a single unit.
- **Inheritance**: A mechanism where one class inherits attributes and methods from another.
- **Polymorphism**: The ability to use a method in multiple ways.
- **Abstraction**: Hiding complex implementation details and showing only necessary features.

## 4. Modules and Packages in Python

- **Module**: A single Python file that contains functions, variables, and classes. It helps in organizing code logically.
- **Package**: A collection of modules in a directory with a special `__init__.py` file that marks the directory as a Python package.
- They help in code organization by dividing functionality into smaller, reusable files.

## 5. Exception Handling in Python

Python uses `try`, `except`, and `finally` blocks to handle exceptions.

Example:

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This will always execute.")
