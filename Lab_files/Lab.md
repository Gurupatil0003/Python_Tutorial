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
