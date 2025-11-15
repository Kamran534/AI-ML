# hello.py - My First Python Program
# Created: [Today's Date]

# Print a welcome message
print("Hello, World!")
print("Welcome to Python Programming!")

# Simple arithmetic
result = 10 + 5
print("10 + 5 =", result)

# Your name (change this to your name)
my_name = "Your Name Here"
print("My name is:", my_name)
print("I am learning Python!")




# Basic printing
print("Hello")

# Multiple values
print("Name:", "Alice", "Age:", 25)

# Special characters
print("Line 1\nLine 2")  # \n = new line
print("Tab\tSeparated")  # \t = tab

# Concatenation
print("Hello" + " " + "World")

# f-strings (formatted strings) - modern way
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old")



# messages.py - String Formatting Practice

name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your hobby: ")

# Create formatted message
message = f"""
╔════════════════════════════════════╗
║        PERSONAL PROFILE            ║
╚════════════════════════════════════╝

Name:    {name}
Age:     {age}
Hobby:   {hobby}

Thank you for sharing, {name}!
"""

print(message)