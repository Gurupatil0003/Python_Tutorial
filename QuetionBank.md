# Python Full Stack Development - Concepts

# Short Answers
## 1. Difference between List and Tuple in Python

| **Aspect**              | **List**                                  | **Tuple**                               |
|-------------------------|-------------------------------------------|-----------------------------------------|
| **Definition**          | Ordered collection of items, mutable.     | Ordered collection of items, immutable. |
| **Syntax**              | Defined with square brackets: `[]`        | Defined with parentheses: `()`          |
| **Mutability**          | Mutable (can be modified after creation). | Immutable (cannot be modified after creation). |
| **Duplicates**          | Allows duplicates.                        | Allows duplicates.                     |
| **Indexing**            | Supports indexing (e.g., `list[0]`).      | Supports indexing (e.g., `tuple[0]`).  |
| **Slicing**             | Supports slicing (e.g., `list[1:3]`).     | Supports slicing (e.g., `tuple[1:3]`). |
| **Methods**             | Supports many methods (e.g., `.append()`, `.pop()`, `.extend()`). | Supports fewer methods (e.g., `.count()`, `.index()`). |
| **Performance**         | Slower than tuples due to its mutability. | Faster than lists due to immutability. |
| **Use Case**            | Used when you need a collection that might change. | Used when you need a collection that won't change. |
| **Memory Consumption**  | Consumes more memory due to mutability.   | Consumes less memory due to immutability. |
| **Example**             | `my_list = [1, 2, 3]`                    | `my_tuple = (1, 2, 3)`                  |


## 2. Different Types of Function Arguments in Python

# Function Arguments in Python

**Function arguments** in Python are the values passed to a function when it is called. They allow functions to accept inputs and perform operations on them.

- **Positional arguments**: Passed by position.
  - Example: `def func(a, b)`, called as `func(1, 2)`

- **Keyword arguments**: Passed by name.
  - Example: `def func(a, b)`, called as `func(a=1, b=2)`

- **Default arguments**: Arguments with default values.
  - Example: `def func(a, b=2)`, called as `func(1)` or `func(1, 3)`

- **Variable-length arguments**: 
  - `*args` for non-keyword variable arguments.
  - `**kwargs` for keyword variable arguments.
  - Example: `def func(*args, **kwargs)`


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

# Long Question 4M each


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

 | **Operation**            | **List**                         | **Set**                           | **Tuple**                         | **Dictionary**                         |
|--------------------------|----------------------------------|-----------------------------------|-----------------------------------|----------------------------------------|
| **Representation**       | `list = [3, 4]`                 | `my_set = {1, 2}`                 | `tuple = (3, 4)`                  | `my_dict = {'a': 1, 'b': 2}`           |
| **Ordered**              | Yes (since Python 3.7)          | No                                | Yes                               | Yes (since Python 3.7)                 |
| **Mutable**              | Yes                              | Yes                               | No                                | Yes                                    |
| **Duplicates allowed**   | Yes                              | No                                | No                                | Keys: No, Values: Yes                 |
| **Indexing**             | Yes <br> Example: `list = [3, 4]`,  <br> `list[0]` → `3` | No                                | Yes <br> Example: `tuple = (3, 4)`, <br>`tuple[0]` → `3` | Yes <br> Example: `my_dict = {'a': 1}`,<br> `my_dict['a']` → `1` |
| **Slicing**              | Yes <br> Example: `list = [3, 4, 5]`, <br>`list[1:3]` → `[4, 5]` | No                                | Yes <br> Example: `tuple = (3, 4, 5)`,<br> `tuple[1:3]` → `(4, 5)` | No (but values can be accessed by key) |
| **Adding elements**      | `.append()`, `.extend()`, `.insert()` <br> Example: `list = [3, 4]`, <br>`list.append(5)` → `list = [3, 4, 5]` | `.add()`, `.update()` <br> Example: `my_set = {1, 2}`, <br>`my_set.add(3)` → `my_set = {1, 2, 3}` | Not applicable                    | `.update()`, `.setdefault()` <br> Example: `my_dict = {'a': 1}`,<br> `my_dict.update({'b': 2})` → `my_dict = {'a': 1, 'b': 2}` |
| **Removing elements**    | `.remove()`, `.pop()`, `.clear()` <br> Example: `list = [3, 4, 5]`,<br> `list.pop()` → `list = [3, 4]` | `.remove()`, `.discard()`, `.pop()` <br> Example: `my_set = {1, 2, 3}`,<br> `my_set.remove(2)` → `my_set = {1, 3}` | Not applicable                    | `.pop()`, `.popitem()`, `.clear()` <br> Example: `my_dict = {'a': 1, 'b': 2}`,<br> `my_dict.pop('a')` → `my_dict = {'b': 2}` |


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
# Long Answer 5M each

# 1.Write a Python program that demonstrates the use of classes and objects.

```python
# Python Program: Demonstrating Classes and Objects

In this example, we will create a `Car` class that represents a car. We will use objects to represent individual cars and demonstrate how to interact with their attributes and methods.

## Code

```python
# Define a class called Car
class Car:
    # Constructor to initialize the car's attributes
    def __init__(self, make, model, year):
        self.make = make  # Brand of the car
        self.model = model  # Model of the car
        self.year = year  # Year of manufacture
        self.mileage = 0  # Initial mileage is set to 0

    # Method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"Mileage: {self.mileage} miles")

    # Method to drive the car and increase its mileage
    def drive(self, miles):
        self.mileage += miles
        print(f"The car has been driven for {miles} miles.")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Display information about the car
my_car.display_info()

# Drive the car for 100 miles
my_car.drive(100)

# Display updated information about the car
my_car.display_info()


```
# What are Python dictionaries? Explain their features and demonstrate how to add, 
 update, and delete items from a dictionary

A **dictionary** in Python is a collection of unordered, changeable, and indexed items. It is used to store data in key-value pairs, where each key is unique. Dictionaries are defined using curly braces `{}`, with keys and values separated by a colon.

## Features of Python Dictionaries

1. **Unordered**: Dictionaries do not maintain any order of elements.
2. **Changeable**: You can add, update, or remove items after the dictionary is created.
3. **Indexed by Keys**: Items are accessed by unique keys, not by numerical index like in lists.
4. **No Duplicate Keys**: Each key in a dictionary must be unique.
5. **Mutable**: Dictionaries are mutable, meaning their contents can be changed.

## Example: Creating and Using a Dictionary

### Code Example

```python
# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Display the dictionary
print("Initial dictionary:", my_dict)

# Adding items to the dictionary
my_dict['email'] = 'john@example.com'  # Add a new key-value pair
print("Dictionary after adding an item:", my_dict)

# Updating an existing item
my_dict['age'] = 26  # Update the value of 'age'
print("Dictionary after updating 'age':", my_dict)

# Deleting an item
del my_dict['city']  # Remove the key 'city'
print("Dictionary after deleting 'city':", my_dict)

# Using the pop() method to remove and return a specific item
removed_item = my_dict.pop('email')  # Remove 'email' and store its value
print("Removed item:", removed_item)
print("Dictionary after pop operation:", my_dict)

# Using the clear() method to remove all items
my_dict.clear()  # Removes all items from the dictionary
print("Dictionary after clear:", my_dict)
```
# What are Access Specifiers in Python?

Access specifiers (also known as access modifiers) are used to define the visibility and accessibility of class members (attributes and methods) in Python. They control how the members of a class can be accessed from outside the class.

Python provides three types of access specifiers:

1. **Public**
2. **Protected**
3. **Private**

## 1. Public Access Specifier

- **Public members** can be accessed from anywhere, both inside and outside the class.
- By default, all members (attributes and methods) are public in Python if no access modifier is specified.

### Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.model = model  # Public attribute

    def display_info(self):  # Public method
        print(f"Car: {self.make} {self.model}")

# Creating an object
car = Car("Toyota", "Corolla")
car.display_info()  # Accessing public method
print(car.make)  # Accessing public attribute
```
# output
```python
Car: Toyota Corolla
Toyota

```

## Protected Access Specifier

- **Protected members** are intended to be used only within the class and its subclasses.
- In Python, a protected member is indicated by a single underscore (`_`) before the attribute or method name.
- Protected members are not strictly enforced in Python, and this is just a convention to indicate that they should not be accessed directly from outside the class. It is a way of telling other developers that these members are internal to the class and should not be accessed directly.

### Example:

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute

    def _display_info(self):  # Protected method
        print(f"Car: {self._make} {self._model}")

# Creating an object
car = Car("Toyota", "Corolla")
car._display_info()  # Accessing protected method (not recommended)
print(car._make)  # Accessing protected attribute (not recommended)

```

# Output
```python
Car: Toyota Corolla
Toyota

```
## Private Access Specifier

- **Private members** can only be accessed within the class they are defined. They cannot be accessed directly from outside the class.
- In Python, a private member is indicated by a double underscore (`__`) before the attribute or method name.
- Private members are **name-mangled**, which means their names are internally changed to include the class name. This makes it harder (but not impossible) to access them from outside the class.

### Example:

```
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)
```
# output
```python
Name: Jessa
Salary: 10000
```

# Write a python program that takes an integer argument and print the table of that 
 integer. Display input error if input value is 0 or –ve.
```python
# Function to print the multiplication table
def print_table(num):
    # Check if the number is 0 or negative
    if num <= 0:
        print("Input Error: Please enter a positive integer greater than 0.")
        return
    
    # Print the table of the number
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Take input from the user
try:
    number = int(input("Enter an integer: "))
    print_table(number)
except ValueError:
    print("Input Error: Please enter a valid integer.")
```
# output
```python
Enter an integer: 5
Multiplication Table of 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

```python
Enter an integer: -3
Input Error: Please enter a positive integer greater than 0.

```

# Describe how to open, read, and write to a file in Python. Provide a program example that writes a string to a text file and then reads the content

Python provides built-in functions to handle files. You can open, read, write, and close files using Python's built-in `open()` function and file methods.

## Opening a File

You can open a file using the `open()` function. This function requires at least one argument: the name of the file you want to open. Additionally, you can specify the mode in which the file should be opened.

### Modes for opening a file:
- **'r'** – Read (default). Opens the file for reading.
- **'w'** – Write. Opens the file for writing (creates a new file or overwrites an existing one).
- **'a'** – Append. Opens the file for appending new content at the end.
- **'r+'** – Read/Write. Opens the file for both reading and writing.

## Writing to a File

To write to a file, you must open it in write (`'w'`) or append (`'a'`) mode. The `write()` method writes a string to the file.

## Reading from a File

To read from a file, open it in read (`'r'`) or read/write (`'r+'`) mode. You can use methods like `read()`, `readline()`, or `readlines()` to fetch data.

## Example Program

The following example demonstrates how to write a string to a text file and then read its contents:

### Code Example:

```python
# Step 1: Write to a file
file_name = "example.txt"
content_to_write = "Hello, this is a test message written to a file."

# Open the file in write mode ('w') and write the content
with open(file_name, 'w') as file:
    file.write(content_to_write)

print(f"Content has been written to {file_name}.")

# Step 2: Read from the file
with open(file_name, 'r') as file:
    content_read = file.read()  # Read the entire content of the file

print(f"Content read from {file_name}:")
print(content_read)
```

# Write a Python program to connect to a MySQL database, create a table, insert data into it, and fetch the data. Explain each step of the process
```python
import mysql.connector

# Step 1: Connect to MySQL Database
try:
    # Establish connection to MySQL database
    connection = mysql.connector.connect(
        host='localhost',       # MySQL server address (localhost for local server)
        user='root',            # MySQL username
        password='yourpassword',# MySQL password (replace with your password)
        database='test_db'      # The database to use
    )

    if connection.is_connected():
        print("Connected to the database")

        # Step 2: Create a Cursor object using the connection
        cursor = connection.cursor()

        # Step 3: Create a table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            position VARCHAR(100)
        )
        '''
        cursor.execute(create_table_query)
        print("Table 'Employees' created successfully (if not exists)")

        # Step 4: Insert data into the table
        insert_query = "INSERT INTO Employees (name, age, position) VALUES (%s, %s, %s)"
        data_to_insert = [
            ("John Doe", 28, "Software Engineer"),
            ("Jane Smith", 34, "Data Scientist"),
            ("Robert Brown", 25, "Product Manager")
        ]
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()  # Commit the transaction
        print(f"{cursor.rowcount} rows inserted into the 'Employees' table.")

        # Step 5: Fetch data from the table
        cursor.execute("SELECT * FROM Employees")
        result = cursor.fetchall()
        
        print("\nFetched Data:")
        for row in result:
            print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\nMySQL connection closed.")
```

# Output
```
Connected to the database
Table 'Employees' created successfully (if not exists)
3 rows inserted into the 'Employees' table.

Fetched Data:
(1, 'John Doe', 28, 'Software Engineer')
(2, 'Jane Smith', 34, 'Data Scientist')
(3, 'Robert Brown', 25, 'Product Manager')

MySQL connection closed.
```

# Creating and Using a Custom Python Package in Python

A **Python package** is a way to organize related Python modules into a directory hierarchy. A package is essentially a folder containing Python files and an `__init__.py` file. The `__init__.py` file makes Python treat the directory as a package and can contain initialization code if needed.

### Steps to Create a Custom Python Package

1. **Create the Package Directory**: This directory will hold the Python modules and the `__init__.py` file.
2. **Create Python Modules**: Each `.py` file will contain functions, classes, or variables that belong to the package.
3. **Create the `__init__.py` File**: This file allows Python to treat the directory as a package. It can be empty or contain package-level initialization code.
4. **Import and Use the Package**: Import the modules from your package and use them in a Python program.

### Example: Creating a Custom Python Package

We will create a package called `mypackage` with two modules:
1. `math_operations.py` – This module will contain functions for addition and subtraction.
2. `string_operations.py` – This module will contain a function to concatenate strings.

### Folder Structure:
```python
mypackage/              <- Package directory
    __init__.py          <- Initialization file
    math_operations.py   <- Module 1
    string_operations.py <- Module 2
example.py              <- Program that uses the package
setup.py                <- Setup script for packaging and installation
```

### Explanation:

1. **mypackage/**: 
   - This is the directory that contains all the files for your custom Python package. It includes your modules and an `__init__.py` file, which is required to treat the directory as a package.

2. **`__init__.py`**:
   - The `__init__.py` file is used to mark the directory as a package. It can be empty or contain package-level initialization code.

3. **`math_operations.py`**:
   - This is the first module of the package that contains functions related to basic math operations, such as `add` and `subtract`.

4. **`string_operations.py`**:
   - The second module of the package, which contains functions related to string operations, such as `concatenate`.

5. **`example.py`**:
   - A Python script that imports and uses the custom package `mypackage`. It demonstrates how to use the functions defined in the package's modules.

6. **`setup.py`**:
   - This is the script used for packaging and distribution. It defines the metadata and configuration for your package, making it easier to distribute and install.

---

### Example `setup.py` file:

```python
from setuptools import setup, find_packages



setup(
    name="mypackage",            # Name of your package
    version="0.1",               # Version number
    packages=find_packages(),    # Automatically find and include all packages
)

```

<div align="center">
<h3> Connect with me<a href="https://gifyu.com/image/Zy2f"><img src="https://github.com/Gurupatil0003/Gurupatil0003/blob/main/Handshake.gif" width="60"></a>
</h3> 

<p align="center">
    <a href="https://www.linkedin.com/in/guranna-gouda-039870228/" target="_blank"><img alt="LinkedIn" width="25px" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Linkedin.svg"></a>
    <a href="https://www.instagram.com/" target="_blank"><img alt="Instagram" width="25px" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Instagram.svg"></a>
    <a href="https://www.facebook.com/" target="_blank"><img alt="Facebook" width="25px" src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"></a>
    <a href="mailto:milaanparmar9@gmail.com" target="_blank"><img alt="Gmail" width="25px" src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Gmail.svg"></a> 
</p>  

