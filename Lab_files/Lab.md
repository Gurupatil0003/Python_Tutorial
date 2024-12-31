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
