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

```
## 6. `try`, `except`, and `finally` Block in Python

- **try**: The block of code where exceptions are anticipated.
- **except**: Catches the exception if raised in the try block.
- **finally**: Executes code regardless of an exception being raised, often used for cleanup.

Example:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleaning up resources.")
```

# Python Full Stack Development - Concepts

## 7. Data Types in Python

Python provides several built-in data types, which are classified into mutable and immutable types.

### Immutable Data Types:
- **int**: Integer values (e.g., `10`, `-5`)
- **float**: Decimal numbers (e.g., `3.14`, `-0.001`)
- **str**: Strings or sequences of characters (e.g., `"Hello"`, `'World'`)
- **tuple**: Immutable sequence (e.g., `(1, 2, 3)`)
- **frozenset**: An immutable version of `set`

### Mutable Data Types:
- **list**: Ordered collection of elements that can be changed (e.g., `[1, 2, 3]`)
- **dict**: A collection of key-value pairs (e.g., `{"name": "John", "age": 30}`)
- **set**: Unordered collection of unique elements (e.g., `{1, 2, 3}`)
- **bytearray**: Mutable sequence of bytes

### Other Data Types:
- **bool**: Boolean type, representing `True` or `False`
- **NoneType**: Represents the absence of a value (`None`)

Understanding these data types is essential for handling data effectively in Python applications.

---

## 8. Constructor for Class `Employee` with Different Access Levels

In Python, we can define a class constructor (`__init__`) to initialize object attributes. Additionally, we can control the access level of the attributes:

- **Public**: Can be accessed from outside the class.
- **Protected**: Should be accessed within the class and its subclasses.
- **Private**: Cannot be accessed outside the class (name mangling is applied).

Example of an `Employee` class with different access levels:

```python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name           # Public: can be accessed directly
        self._age = age            # Protected: conventionally used for internal access
        self.__salary = salary     # Private: can't be accessed directly from outside

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

# Creating an object of Employee class
emp = Employee("John Doe", 30, 50000)

# Accessing the public attribute
print(emp.name)  # Works fine

# Accessing the protected attribute (should be avoided outside the class)
print(emp._age)

# Accessing the private attribute (will result in an error)
# print(emp.__salary)  # Uncommenting this will raise an AttributeError
```
## 9. What is base class and derived class in python ? Explain with an example.

In Object-Oriented Programming (OOP), a base class is a class that is inherited by other classes, known as derived classes. The derived class inherits attributes and methods from the base class but can also define its own methods and override base class methods.
```pyton
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Derived class
    def speak(self):  # Method overriding
        print(f"{self.name} barks.")

class Cat(Animal):  # Derived class
    def speak(self):  # Method overriding
        print(f"{self.name} meows.")

# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Outputs: Buddy barks.
cat.speak()  # Outputs: Whiskers meows.
```

## 10. Role of Conditional Statements in Python

Conditional statements in Python are used to execute certain blocks of code based on whether a condition is true or false. They allow the program to make decisions and follow different execution paths. This is essential for creating dynamic and flexible programs.

### Types of Conditional Statements:
- **if**: Executes a block of code if the condition is true.
- **elif**: Checks another condition if the previous `if` or `elif` condition is false.
- **else**: Executes a block of code if none of the `if` or `elif` conditions are true.

### Syntax:
```python
if condition:
    # Execute this block if condition is true
elif another_condition:
    # Execute this block if another_condition is true
else:
    # Execute this block if none of the above conditions are true
```
### Example
```python
age = 20

if age < 18:
    print("Underage")
elif age == 18:
    print("Just turned adult")
else:
    print("Adult")

```
## 12. Purpose of the `__init__.py` File in Python Packages

The `__init__.py` file is a special Python file that marks a directory as a Python package. Without this file, Python will treat the directory as a normal folder and not as a package. 

### Purpose:
- **Package Initialization**: The `__init__.py` file can be empty, but it is often used to initialize the package and import specific modules or functions when the package is imported.
- **Organizing Code**: By using `__init__.py`, you can organize your code into packages and sub-packages for better modularity.
- **Making Code Reusable**: It allows you to structure your project in a way that you can reuse your modules by importing them as a package.

### Syntax of `__init__.py`:
```python
# __init__.py
# This can be an empty file or can contain initialization code for the package.

# Example: Import specific modules or functions when the package is imported
from .module1 import function1
from .module2 import function2
```
### Structure For package

```
my_package/
    __init__.py         # Initializes the package and imports functions
    module1.py          # Contains function1
    module2.py          # Contains function2
setup.py
main.py

```




## 2. What is Inheritance in Python? Explain Different Types of Inheritance with an Example

### What is Inheritance?

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class (called the **derived class** or **child class**) to inherit attributes and methods from another class (called the **base class** or **parent class**). The derived class can override or extend the functionality of the base class, promoting code reuse and making the code easier to maintain.

### Types of Inheritance in Python

There are several types of inheritance in Python:

1. **Single Inheritance**
2. **Multiple Inheritance**
3. **Multilevel Inheritance**
4. **Hierarchical Inheritance**
5. **Hybrid Inheritance**

## 3. Python's File Handling Mechanism

Python provides built-in functions and methods to work with files. File handling in Python is done through the `open()` function, which returns a file object. This file object allows us to read or write to the file. Python supports different file modes for opening a file, such as read mode (`r`), write mode (`w`), append mode (`a`), and more.

### File Modes
- **`r`**: Read (default mode) – Opens the file for reading. The file pointer is at the beginning of the file.
- **`w`**: Write – Opens the file for writing. If the file does not exist, it creates a new file. If the file exists, it overwrites the file.
- **`a`**: Append – Opens the file for writing. If the file does not exist, it creates a new file. If the file exists, it appends to the end of the file.
- **`rb`**: Read binary – Opens the file in binary mode for reading.
- **`wb`**: Write binary – Opens the file in binary mode for writing.

### 1. Opening a File

The `open()` function is used to open a file. It accepts two parameters:
1. **filename**: The name of the file you want to open.
2. **mode**: The mode in which you want to open the file (e.g., `'r'`, `'w'`, `'a'`).

Syntax:
```python
file = open('file_name', 'mode')  # Open the file in read mode
```

### Reading file
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```
### Writeing File
```python
with open('example.txt', 'w') as file:
    file.write('Hello, world!\nThis is a new line.')
```

## 4.(1) Write a command that insert multiple documents in mongodb database (database name: voteDb). Each document must have at least 2 or more keys.

- To insert multiple documents into MongoDB using Python, first connect to the MongoDB server using MongoClient(), then select the target database and collection. Use insert_many() to add the documents to the 
  collection.
```python
pip install pymongo
```

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally on the default port

# Select the 'voteDb' database and 'votes' collection
db = client["voteDb"]
collection = db["votes"]

# Documents to insert
documents = [
    { "candidate": "John Doe", "votes": 1200 },
    { "candidate": "Jane Smith", "votes": 1500 },
    { "candidate": "Sam Brown", "votes": 800 },
    { "candidate": "Emily Clark", "votes": 950 }
]

# Insert multiple documents
insert_result = collection.insert_many(documents)

# Print the inserted IDs
print(f"Inserted document IDs: {insert_result.inserted_ids}")
```

# Python String Module Functions

This document explains some useful functions from Python's `string` module, which provides a collection of string constants and utility functions.

## 1. `string.ascii_letters`

### Description:
`string.ascii_letters` is a constant that contains all the lowercase and uppercase letters of the alphabet (`a-z` and `A-Z`).

### Example:
```python
import string

print(string.ascii_letters)
```
### Output

```python
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

```
## 2. `string.ascii_letters`

### Description:

string.punctuation is a constant that contains all the punctuation characters, including symbols like `!"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`.`

### Example:
```python
iimport string

print(string.punctuation)

```
### Output

```python
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

# 6.(3) Explain polymorphism feature of python with an example code.

**Polymorphism** is a core concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. The most common use of polymorphism in Python is when a parent class reference is used to refer to objects of different child classes.

In Python, polymorphism allows you to define methods in the child classes that have the same name as methods in the parent class, but the method's behavior can be different depending on the object calling it.

### Key Points:
- **Method Overriding**: Child classes can override the methods of the parent class.
- **Duck Typing**: In Python, polymorphism works through method name matching rather than explicit interfaces.

## Example Code

```python
# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound")

# Child class 1
class Dog(Animal):
    def speak(self):
        print("The dog barks")

# Child class 2
class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Child class 3
class Cow(Animal):
    def speak(self):
        print("The cow moos")

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrating polymorphism
def animal_sound(animal):
    animal.speak()

# Passing different objects to the same function
animal_sound(animal)  # Output: The animal makes a sound
animal_sound(dog)     # Output: The dog barks
animal_sound(cat)     # Output: The cat meows
animal_sound(cow)     # Output: The cow moos
```
# Output
```python
The animal makes a sound
The dog barks
The cat meows
The cow moos

```
## 7.Describe the differences between lists, sets, tuples, and dictionaries in Python. Provide
  an example for each. 
![image](https://github.com/user-attachments/assets/fddf927e-3b53-4c9c-a39f-6a928309892e)

# 8.Explain the significance of the with statement in Python for file handling. Provide an
 example.

# The Significance of the `with` Statement in Python for File Handling

The **`with`** statement in Python is used to wrap the execution of a block of code. It simplifies exception handling and resource management, particularly when dealing with file operations. The **`with`** statement is often referred to as a **context manager** and ensures that resources are properly cleaned up after use, even in the event of an error.

When working with files, it is important to close the file after it has been used to free up system resources. The **`with`** statement automatically takes care of closing the file once the block of code is executed, eliminating the need to explicitly call `file.close()`.

### Significance of `with`:
- **Automatic Resource Management**: It ensures that the file is closed automatically after the block is executed, even if an exception is raised.
- **Cleaner Code**: It reduces the need for explicit `try`-`finally` blocks to close files, making the code more concise and readable.
- **Error Handling**: It manages exceptions gracefully, ensuring that resources are cleaned up even if an error occurs.

### Example Code:

```python
# Using 'with' for file handling
file_name = "example.txt"

# Writing to a file using the 'with' statement
with open(file_name, 'w') as file:
    file.write("Hello, world!\nThis is a file handling example.")

# Reading from a file using the 'with' statement
with open(file_name, 'r') as file:
    content = file.read()
    print(content)

```
# 9.Describe how the try, except, and finally blocks are used in Python to handle exceptions
 with an example.

In Python, exceptions are events that can disrupt the normal flow of a program. Exception handling allows you to gracefully handle errors and maintain control over program execution. The `try`, `except`, and `finally` blocks are used together to catch exceptions and perform necessary cleanup actions.

### Key Concepts:
- **`try` Block**: The code that may raise an exception is placed inside the `try` block.
- **`except` Block**: If an exception is raised inside the `try` block, the code inside the `except` block is executed to handle the exception.
- **`finally` Block**: This block is always executed, regardless of whether an exception occurred or not. It is typically used for cleanup operations (e.g., closing files or releasing resources).

### Syntax:
```python
try:
    # Code that may cause an exception
    pass
except <ExceptionType> as e:
    # Code to handle the exception
    pass
finally:
    # Code that always executes (cleanup actions)
    pass
```

# Example
```python
try:
    # Attempting to divide by zero
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This will always execute.")

```
# Output
```python
Error: division by zero
This will always execute.

```

