# Exercise 1: Define a function that accepts 2 values and return its sum, subtraction and multiplication.


## Hint
Input:
Enter value of a = 7
Enter value of b = 5


## Expected output

| Operation         | Result |
|-------------------|--------|
| Sum               | 12     |
| Subtraction       | 2      |
| Multiplication    | 35     |


# solution
def result(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    print(f"Sum is {sum}, Sub is {sub}, & Multiply is {mul}")

a = int(input("Enter value of a: "))  # 7
b = int(input("Enter value of b: "))  # 5
result(a,b)

# Exercise 2: Define a function that accepts roll number and returns whether the student is present or absent. 

## Hint
Use a list to store sample roll. no.
Get input from a user and check if the number
exist in the list or not, if exists return present
else return absent

## solution
def detail(roll):
    x = [23,43,22,56]
    if roll in x:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")
roll = int(input("Enter roll no. ")) # 24
detail(roll)

# output
# Roll number 24 is absent

# Exercise 3: Define a function in python that accepts 3 values and returns the maximum of three numbers.

Hint
Input:
Value of a = 30
Value of b = 22
value of c = 18

Expected output 
30 is the maximum among all


## Sollution

def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum among all")
    elif b > a and b > c:
        print(f"{b} is maximum among all")
    else:
        print(f"{c} is maximum among all")

max(30,22,18)

# Exercise 4: Define a function that accepts a number and returns whether the number is even or odd.

Hint
Input:
Enter a number = 4

Expected output 
4 is an even number

Hint
Input:
Enter a number = 5

Expected output 
4 is an odd number
## Solution 

def func(x):
    if x % 2 == 0:
        print(f"{x} is Even number")
    else:
        print(f"{x} is Odd number")
x = int(input("Enter a number "))
func(4)

# Exercise 5: Define a function which counts vowels and consonant in a word.
Hint
Input:
Enter a word = pythonlobby

Expected output 
Count of vowel is = 2
Count of consonant is = 9

## Solution
def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
        else:
            con = con + 1

    print("Count of vowels is ",vov)
    print("Count of consonant is ",con)

x = input("Enter Value: ") # pythonlobby
count(x)

# Exercise 6: Define a function that returns Factorial of a number.
Hint
Input:
Enter a number = 6

Expected output 
Factorial is 720

# Solution
def factorial(num):
    fact = 1
    while(num!=0):
        fact *= num
        num = num - 1
    print("Factorial is",fact)

num = int(input("Enter number "))
factorial(num)

# Exercise 7: Define a function that accepts lowercase words and returns uppercase words.
Hint
Input:
Enter a word = pythonlobby

Expected output 
Result is = PYTHONLOBBY

# Solution
def response(text):
    z = text.upper()
    print(z)

text = input("Enter String: ")  # pythonlobby
response(text)

# 8. Write a program which can map() to make a list whose elements are cube of elements in a given list
def cube(lst):
    """
    Returns the list of cubes of given number
    """
    return list(map(lambda x: x**3, lst))

cube([1, 3, 5, 9, 15])

# 1: Suggest Footwear
# Write a program that will give suggested footwear based on the weather.
# Ask the user for the weather outside with three options (sunny, rainy, or snowy) and give the correct footwear suggestion (sneaker, gumboot, or boots). Each # # # option should be written as its own function that prints a message based on the input.
def sunny():
    print("It is sunny day, good to wear sneaker!")
 
def rainy():
    print("Oops! its raining, better wear gumbot")
 
def snowy():
    print("Wow! its snowing, better wear boot")
 
weather_today = input("Whats the weather today:")
if weather_today == "sunny":
    sunny()
elif weather_today == "rainy":
    rainy()
elif weather_today == "snowy":
    snowy()
else:
    print(f"No footwear avaibale for {weather_today}")


# My Favorite Book
# Write a function called favorite_book() that accepts two parameter, title and author. The function should print a message, such as The History of Bhutan by Karma # Phuntsho. Call the function, make sure to include a book title and author as an argument in the function call.    
def favorite_book(title, author):
   print(f"{title} was written by {author}")
favorite_book("The History of Bhutan", "Karma Phuntsho")
