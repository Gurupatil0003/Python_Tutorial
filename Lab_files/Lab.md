~~~python
import random
import string

print("Random Password Generator")
length = int(input("Enter the desired length for the password: "))
if length > 0:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    print(f"Generated Password: {password}")
else:
    print("Invalid password length. Please enter a positive integer.")
~~~

~~~python

import pandas as pd

# Define a function to display the entire table (DataFrame) from the CSV file
def display_table(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Display the entire DataFrame (table)
    print("The entire table:")
    print(df)

# Example usage
file_path = "your_file.csv"  # Replace with the path to your CSV file
display_table(file_path)

~~~

~~~python
import pandas as pd

# Define a function to calculate the mean of a specified column
def calculate_mean(file_path, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Calculate and return the mean of the specified column
        return df[column_name].mean()
    else:
        # Return a message if the column doesn't exist
        return f"Column '{column_name}' not found in the file."

# Example usage
file_path = "your_file.csv"  # Replace with the path to your CSV file
column_name = "Specified column"  # Replace with your column name
mean_value = calculate_mean(file_path, column_name)

print(mean_value)

~~~

```python
class Person:
    def __init__(self, name, role, detail):
        self.name = name
        self.role = role
        self.detail = detail

    def get_details(self):
        return f"{self.role} Name: {self.name}, {self.detail}"

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def list_students(self):
        return [student.name for student in self.students]

# Example usage:
student = Person("John", "Student", "Grade: 10")
teacher = Person("Guru Sir", "Teacher", "Subject: Python")

course = Course("Python Programming", teacher)
course.enroll_student(student)

# Print details
print(student.get_details())
print(f"Enrolled in {course.name} taught by {teacher.name}")



```
