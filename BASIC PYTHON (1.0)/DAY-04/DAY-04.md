# Day 4: Control Flow - Loops (for & while)

**Duration:** 3-4 hours | **Date:** _________ | **Status:** ⬜ Not Started | ⬜ In Progress | ⬜ Completed

---

## 🎯 Today's Goals

By the end of today, you will:
- ✅ Understand loop concepts and iteration
- ✅ Master for loops with range()
- ✅ Master while loops
- ✅ Use break, continue, and pass statements
- ✅ Write nested loops
- ✅ Create loop-based patterns and programs
- ✅ Complete 8+ practical projects

---

## 📋 Pre-Session Checklist

Before starting:
- [ ] Completed Days 1-3
- [ ] Understand if/elif/else statements
- [ ] Know comparison and logical operators
- [ ] Can use variables and data types
- [ ] Have Python and VS Code ready

**Quick Review Test:**
```python
# Can you predict the output?
for i in range(5):
    print(i)
# What numbers will print?
```

---

## 🕐 Session 1: Introduction to Loops & for Loops (60 minutes)

### Part 1.1: What are Loops?

**Concept:**
Loops allow you to execute code repeatedly without writing it multiple times.

**Without Loops (Repetitive):**
```python
print("Hello 1")
print("Hello 2")
print("Hello 3")
print("Hello 4")
print("Hello 5")
```

**With Loops (Efficient):**
```python
for i in range(1, 6):
    print(f"Hello {i}")
```

### Part 1.2: The for Loop

**Basic Syntax:**
```python
for variable in sequence:
    # Code block to repeat
    statement1
    statement2
```

**Simple Examples:**
```python
# Example 1: Print numbers 0 to 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Example 2: Print numbers 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Example 3: Print even numbers
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10

# Example 4: Countdown
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
# Output: 10, 9, 8, ..., 1, Blast off!
```

### Part 1.3: Understanding range()

**range() Function Syntax:**
```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1, increment by step
```

**Examples:**
```python
# range(stop)
print(list(range(5)))
# [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 8)))
# [2, 3, 4, 5, 6, 7]

# range(start, stop, step)
print(list(range(0, 20, 5)))
# [0, 5, 10, 15]

# Negative step (counting down)
print(list(range(10, 0, -1)))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Negative numbers
print(list(range(-5, 5)))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
```

### Part 1.4: for Loop Applications

**Example 1: Sum of Numbers**
```python
# Calculate sum of 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}")
# Output: 5050
```

**Example 2: Multiplication Table**
```python
# Multiplication table for 5
number = 5
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```

**Example 3: Factorial**
```python
# Calculate factorial of a number
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
# Output: 5! = 120
```

**Example 4: Counting Characters**
```python
# Count vowels in a string
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
# Output: 3 (e, o, o)
```

**Example 5: Iterating Over Strings**
```python
# Print each character
word = "Python"
for letter in word:
    print(letter)
# Output: P, y, t, h, o, n (each on new line)

# With index
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")
```

**Example 6: Building Patterns**
```python
# Print a triangle
for i in range(1, 6):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****

# Numbered triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

### Practice Exercise 1: for Loop Basics

Create `for_loops_practice.py`:
```python
# for_loops_practice.py - Practice for Loops

print("=== EXERCISE 1: Print Even Numbers ===")
# Print all even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

print("=== EXERCISE 2: Sum of Squares ===")
# Calculate sum of squares from 1 to 10
total = 0
for i in range(1, 11):
    total += i ** 2
print(f"Sum of squares 1² + 2² + ... + 10² = {total}")
print()

print("=== EXERCISE 3: Reverse String ===")
text = "Python"
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")
print()

print("=== EXERCISE 4: Count Digits ===")
number = 123456
digit_count = 0
temp = number
while temp > 0:  # We'll learn while loops soon
    digit_count += 1
    temp //= 10
print(f"Number of digits in {number}: {digit_count}")
print()

print("=== EXERCISE 5: Temperature Conversion Table ===")
print("Celsius  |  Fahrenheit")
print("-" * 25)
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:>7}°C  |  {fahrenheit:>7.1f}°F")
print()

print("=== EXERCISE 6: FizzBuzz (1-30) ===")
# Print numbers 1-30, but:
# - Print "Fizz" for multiples of 3
# - Print "Buzz" for multiples of 5
# - Print "FizzBuzz" for multiples of both
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print("\n")

print("=== EXERCISE 7: Prime Number Checker ===")
num = 17
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is {'prime' if is_prime else 'not prime'}")
```

### 📹 Video Resources:

1. **"Python for Loops"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
   - Duration: 11 minutes
   - Covers: for loops, range(), iteration

2. **"Python Loops Tutorial"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=94UHCEmprCY
   - Duration: 9 minutes
   - Covers: for loops with practical examples

3. **"For Loops in Python"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=OnDr4J2UXSA
   - Duration: 10 minutes
   - Covers: Iteration, range(), common patterns

### 📚 Text Resources:

1. **Python Official Tutorial - for Statements**
   - Link: https://docs.python.org/3/tutorial/controlflow.html#for-statements
   - Official documentation

2. **Real Python - Python for Loops**
   - Link: https://realpython.com/python-for-loop/
   - Comprehensive guide with examples

3. **W3Schools - Python For Loops**
   - Link: https://www.w3schools.com/python/python_for_loops.asp
   - Interactive examples

### ✅ Checkpoint 1:
- [ ] Understand for loop syntax
- [ ] Can use range() with different arguments
- [ ] Can iterate over strings
- [ ] Completed basic exercises
- [ ] Created at least one pattern

---

## 🕑 Session 2: while Loops & Loop Control (60 minutes)

### Part 2.1: The while Loop

**Basic Syntax:**
```python
while condition:
    # Code block to repeat
    statement1
    statement2
```

**Simple Examples:**
```python
# Example 1: Count to 5
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1, 2, 3, 4, 5

# Example 2: User input validation
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Example 3: Sum until zero
total = 0
number = int(input("Enter number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter number (0 to stop): "))
print(f"Total: {total}")

# Example 4: Countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
```

### Part 2.2: for vs while Loops

**Use for loop when:**
- You know the number of iterations
- Iterating over a sequence (string, list, range)

**Use while loop when:**
- Number of iterations is unknown
- Looping based on a condition
- Getting user input until valid

**Examples Showing Difference:**

```python
# for loop - known iterations
for i in range(5):
    print(i)

# while loop - same result
i = 0
while i < 5:
    print(i)
    i += 1

# while loop - unknown iterations
response = ""
while response.lower() != "yes":
    response = input("Do you want to continue? (yes/no): ")

# for loop - iterating over string
for char in "Python":
    print(char)

# while loop - same result
text = "Python"
i = 0
while i < len(text):
    print(text[i])
    i += 1
```

### Part 2.3: Infinite Loops

**Warning: Infinite Loops**
```python
# ⚠️ INFINITE LOOP - Don't run without break!
# while True:
#     print("This will run forever!")

# Correct way - with break condition
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

**Preventing Infinite Loops:**
```python
# ❌ Wrong - forgot to increment
count = 0
# while count < 5:  # INFINITE - count never changes
#     print(count)

# ✅ Correct
count = 0
while count < 5:
    print(count)
    count += 1

# ❌ Wrong - condition always true
# while 5 > 3:  # INFINITE - 5 is always > 3
#     print("Loop")

# ✅ Correct - condition can become false
x = 10
while x > 3:
    print(x)
    x -= 1
```

### Part 2.4: break Statement

**Using break:**
```python
# Example 1: Exit loop early
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Output: 1, 2, 3, 4 (stops at 5)

# Example 2: Find first divisor
number = 15
for i in range(2, number):
    if number % i == 0:
        print(f"First divisor of {number} is {i}")
        break
else:
    print(f"{number} is prime")

# Example 3: Password attempts
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "secret123":
        print("Login successful!")
        break
    attempts += 1
    print(f"Wrong password. {max_attempts - attempts} attempts remaining")
else:
    print("Account locked!")

# Example 4: Search in string
text = "Python Programming"
search = "gram"
found = False
for i in range(len(text) - len(search) + 1):
    if text[i:i+len(search)] == search:
        print(f"Found '{search}' at position {i}")
        found = True
        break
if not found:
    print(f"'{search}' not found")
```

### Part 2.5: continue Statement

**Using continue:**
```python
# Example 1: Skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1, 3, 5, 7, 9 (skips even numbers)

# Example 2: Skip specific values
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Output: 1, 2, 3, 4, 6, 7, 8, 9, 10 (skips 5)

# Example 3: Process only valid input
numbers = [10, -5, 20, 0, 15, -3, 25]
total = 0
for num in numbers:
    if num <= 0:
        continue  # Skip non-positive numbers
    total += num
print(f"Sum of positive numbers: {total}")

# Example 4: Skip vowels
text = "Hello World"
result = ""
for char in text:
    if char.lower() in "aeiou":
        continue
    result += char
print(f"Without vowels: {result}")
# Output: Hll Wrld
```

### Part 2.6: pass Statement

**Using pass:**
```python
# pass is a placeholder for future code

# Example 1: Empty loop (to be implemented later)
for i in range(5):
    pass  # TODO: Add logic later

# Example 2: Conditional with pass
number = 10
if number > 5:
    pass  # Will implement logic later
else:
    print("Number is 5 or less")

# Example 3: Function placeholder
def future_function():
    pass  # Will implement later

# Example 4: Class placeholder
class MyClass:
    pass  # Will add methods later
```

### Part 2.7: Loop else Clause

**The else with Loops:**
```python
# else executes if loop completes normally (no break)

# Example 1: Search with else
numbers = [2, 4, 6, 8, 10]
search = 7

for num in numbers:
    if num == search:
        print(f"Found {search}")
        break
else:
    print(f"{search} not found in list")
# Output: 7 not found in list

# Example 2: Prime number checker
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")
# Output: 17 is prime

# Example 3: Password validation
correct_password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    attempts += 1
else:
    print("Too many failed attempts. Account locked.")
```

### Practice Exercise 2: while Loops & Control

Create `while_loops_practice.py`:
```python
# while_loops_practice.py - Practice while Loops

print("=== EXERCISE 1: Guessing Game ===")
import random
secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input(f"Guess the number (1-10), {max_attempts - attempts} attempts left: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 Correct! You won in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game over! The number was {secret_number}")
print()

print("=== EXERCISE 2: Input Validation ===")
while True:
    age = input("Enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    if not age.isdigit():
        print("Please enter a valid number!")
        continue
    age = int(age)
    if age < 0 or age > 120:
        print("Age must be between 0 and 120!")
        continue
    print(f"✓ Valid age: {age}")
    break
print()

print("=== EXERCISE 3: Multiplication Quiz ===")
correct = 0
total = 5

for i in range(total):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    
    while True:
        try:
            answer = int(input(f"What is {num1} × {num2}? "))
            break
        except ValueError:
            print("Please enter a number!")
    
    if answer == correct_answer:
        print("✓ Correct!")
        correct += 1
    else:
        print(f"✗ Wrong! The answer is {correct_answer}")

print(f"\nScore: {correct}/{total} ({correct/total*100:.0f}%)")
print()

print("=== EXERCISE 4: Fibonacci Sequence ===")
limit = 100
a, b = 0, 1
print("Fibonacci numbers up to 100:")
while a <= limit:
    print(a, end=" ")
    a, b = b, a + b
print("\n")

print("=== EXERCISE 5: Digital Root ===")
# Keep summing digits until single digit
number = 12345
print(f"Finding digital root of {number}:")
while number >= 10:
    digit_sum = 0
    temp = number
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    print(f"{number} → sum of digits = {digit_sum}")
    number = digit_sum
print(f"Digital root: {number}")
```

### 📹 Video Resources:

1. **"Python while Loops"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
   - Duration: 9 minutes
   - Covers: while loops, break, continue

2. **"Break and Continue"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=yCZBnjF4_tU
   - Duration: 7 minutes
   - Covers: Loop control statements

3. **"Python While Loops"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=HZARImviDxg
   - Duration: 8 minutes

### 📚 Text Resources:

1. **Python Docs - while Loops**
   - Link: https://docs.python.org/3/reference/compound_stmts.html#while

2. **Real Python - while Loops**
   - Link: https://realpython.com/python-while-loop/

### ✅ Checkpoint 2:
- [ ] Understand while loop syntax
- [ ] Know when to use for vs while
- [ ] Can use break statement
- [ ] Can use continue statement
- [ ] Understand loop else clause
- [ ] Completed while loop exercises

---

## 🕒 Session 3: Nested Loops & Projects (90 minutes)

### Part 3.1: Nested Loops

**Concept:**
A loop inside another loop. Inner loop completes all iterations for each iteration of outer loop.

**Basic Pattern:**
```python
for i in range(3):      # Outer loop runs 3 times
    for j in range(2):  # Inner loop runs 2 times for each outer iteration
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

**Example 1: Multiplication Table**
```python
print("MULTIPLICATION TABLE (1-10)")
print("-" * 50)

# Header row
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
print("-" * 50)

# Table rows
for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
```

**Example 2: Pattern Printing**
```python
# Right triangle
print("Right Triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Pyramid
print("\nPyramid:")
n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Diamond
print("\nDiamond:")
n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**Example 3: Finding Pairs**
```python
# Find all pairs that sum to 10
target = 10
for i in range(1, target):
    for j in range(i, target):
        if i + j == target:
            print(f"{i} + {j} = {target}")
```

**Example 4: Nested while Loops**
```python
# Print a grid
rows = 5
cols = 4
i = 0
while i < rows:
    j = 0
    while j < cols:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
```

### Project 1: Number Pyramid Generator

Create `number_pyramid.py`:
```python
# number_pyramid.py - Generate Various Number Patterns

print("="*60)
print("         NUMBER PYRAMID GENERATOR")
print("="*60)

# Pattern 1: Simple Number Pyramid
print("\nPattern 1: Simple Number Pyramid")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Pattern 2: Centered Number Pyramid
print("\nPattern 2: Centered Number Pyramid")
n = 5
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers ascending
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 3: Number Diamond
print("\nPattern 3: Number Diamond")
n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 4: Floyd's Triangle
print("\nPattern 4: Floyd's Triangle")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# Pattern 5: Pascal's Triangle
print("\nPattern 5: Pascal's Triangle")
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def binomial(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = 6
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(binomial(i, j), end="  ")
    print()
```

### Project 2: Simple Calculator with Menu

Create `loop_calculator.py`:
```python
# loop_calculator.py - Calculator with Loop Menu

print("="*60)
print("         PYTHON CALCULATOR")
print("="*60)

while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")
    print("-" * 40)
    
    choice = input("Select operation (1-8): ")
    
    if choice == "8":
        print("\nThank you for using Python Calculator!")
        print("Goodbye! 👋")
        break
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("❌ Invalid choice! Please select 1-8")
        continue
    
    # Get numbers based on operation
    if choice == "6":  # Square root needs only one number
        while True:
            try:
                num = float(input("Enter number: "))
                break
            except ValueError:
                print("❌ Please enter a valid number!")
    else:
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("❌ Please enter valid numbers!")
    
    # Perform calculation
    if choice == "1":
        result = num1 + num2
        print(f"\n✓ {num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"\n✓ {num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"\n✓ {num1} × {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("\n❌ Error: Division by zero!")
        else:
            result = num1 / num2
            print(f"\n✓ {num1} ÷ {num2} = {result}")
    elif choice == "5":
        result = num1 ** num2
        print(f"\n✓ {num1} ^ {num2} = {result}")
    elif choice == "6":
        if num < 0:
            print("\n❌ Error: Cannot calculate square root of negative number!")
        else:
            result = num ** 0.5
            print(f"\n✓ √{num} = {result}")
    elif choice == "7":
        result = (num1 / 100) * num2
        print(f"\n✓ {num1}% of {num2} = {result}")
    
    # Ask if user wants to continue
    continue_calc = input("\nPerform another calculation? (yes/no): ").lower()
    if continue_calc != "yes":
        print("\nThank you for using Python Calculator!")
        break
```

### Project 3: Prime Number Finder

Create `prime_finder.py`:
```python
# prime_finder.py - Find Prime Numbers in Range

print("="*60)
print("         PRIME NUMBER FINDER")
print("="*60)

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    print("\n--- MENU ---")
    print("1. Check if a number is prime")
    print("2. Find all primes in a range")
    print("3. Find first N prime numbers")
    print("4. Prime factorization")
    print("5. Exit")
    
    choice = input("\nSelect option (1-5): ")
    
    if choice == "5":
        print("\nGoodbye!")
        break
    
    if choice == "1":
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"✓ {num} is PRIME")
        else:
            print(f"✗ {num} is NOT prime")
    
    elif choice == "2":
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        
        primes = []
        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(num)
        
        if primes:
            print(f"\nPrime numbers between {start} and {end}:")
            for i, prime in enumerate(primes):
                print(prime, end=" ")
                if (i + 1) % 10 == 0:
                    print()  # New line every 10 numbers
            print(f"\n\nTotal: {len(primes)} prime numbers")
        else:
            print(f"\nNo prime numbers found between {start} and {end}")
    
    elif choice == "3":
        n = int(input("How many prime numbers? "))
        
        primes = []
        num = 2
        while len(primes) < n:
            if is_prime(num):
                primes.append(num)
            num += 1
        
        print(f"\nFirst {n} prime numbers:")
        for i, prime in enumerate(primes):
            print(prime, end=" ")
            if (i + 1) % 10 == 0:
                print()
        print()
    
    elif choice == "4":
        num = int(input("Enter a number to factorize: "))
        original = num
        factors = []
        
        # Find prime factors
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        
        if factors:
            print(f"\nPrime factorization of {original}:")
            print(" × ".join(map(str, factors)))
        else:
            print(f"\n{original} is 1 (no prime factors)")
    
    else:
        print("❌ Invalid choice!")
    
    input("\nPress Enter to continue...")
```

### Project 4: Text-Based Tic-Tac-Toe

Create `tic_tac_toe.py`:
```python
# tic_tac_toe.py - Simple Tic-Tac-Toe Game

print("="*60)
print("         TIC-TAC-TOE GAME")
print("="*60)

def print_board(board):
    """Display the game board"""
    print("\n")
    for i in range(3):
        print(" ", board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("  ---|---|---")
    print("\n")

def check_winner(board, player):
    """Check if player has won"""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False

def is_board_full(board):
    """Check if board is full"""
    return all(spot != " " for spot in board)

# Initialize game
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

print("\nPositions are numbered 1-9:")
temp_board = [str(i) for i in range(1, 10)]
print_board(temp_board)

print("Let's start the game!")

# Main game loop
while not game_over:
    print_board(board)
    
    # Get player move
    while True:
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): "))
            if move < 1 or move > 9:
                print("❌ Please enter a number between 1 and 9!")
                continue
            if board[move - 1] != " ":
                print("❌ That position is already taken!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Make move
    board[move - 1] = current_player
    
    # Check for winner
    if check_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} WINS!")
        game_over = True
    elif is_board_full(board):
        print_board(board)
        print("It's a TIE! 🤝")
        game_over = True
    else:
        # Switch player
        current_player = "O" if current_player == "X" else "X"

print("\nThanks for playing!")
```

### Project 5: Password Strength Analyzer

Create `password_analyzer.py`:
```python
# password_analyzer.py - Analyze Password Strength

print("="*60)
print("      PASSWORD STRENGTH ANALYZER")
print("="*60)

def analyze_password(password):
    """Analyze password and return score and feedback"""
    score = 0
    feedback = []
    
    # Check length
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append("✓ Great length (12+ characters)")
    elif length >= 8:
        score += 2
        feedback.append("✓ Good length (8-11 characters)")
    else:
        score += 1
        feedback.append("✗ Too short (less than 8 characters)")
    
    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Add uppercase letters")
    
    # Check for lowercase
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Add lowercase letters")
    
    # Check for digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Add numbers")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break
    if has_special:
        score += 2
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Add special characters (!@#$%^&* etc.)")
    
    # Check for common patterns (simple check)
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    is_common = False
    for common in common_passwords:
        if common in password.lower():
            is_common = True
            break
    if is_common:
        score -= 2
        feedback.append("✗ Contains common password pattern")
    
    # Determine strength
    if score >= 8:
        strength = "VERY STRONG 🛡️"
        color = "green"
    elif score >= 6:
        strength = "STRONG 💪"
        color = "blue"
    elif score >= 4:
        strength = "MODERATE ⚠️"
        color = "yellow"
    else:
        strength = "WEAK ❌"
        color = "red"
    
    return score, strength, feedback

# Main program
while True:
    print("\n" + "-"*60)
    password = input("Enter password to analyze (or 'quit' to exit): ")
    
    if password.lower() == 'quit':
        print("\nGoodbye!")
        break
    
    if not password:
        print("❌ Password cannot be empty!")
        continue
    
    score, strength, feedback = analyze_password(password)
    
    # Display results
    print("\n" + "="*60)
    print("           PASSWORD ANALYSIS RESULTS")
    print("="*60)
    print(f"Password: {'*' * len(password)}")
    print(f"Length: {len(password)} characters")
    print(f"Score: {score}/10")
    print(f"Strength: {strength}")
    print("\n--- DETAILED FEEDBACK ---")
    for item in feedback:
        print(f"  {item}")
    print("="*60)
    
    # Suggestions
    if score < 6:
        print("\n💡 SUGGESTIONS TO IMPROVE:")
        if len(password) < 12:
            print("  • Make it at least 12 characters long")
        if score < 4:
            print("  • Mix uppercase and lowercase letters")
            print("  • Add numbers and special characters")
            print("  • Avoid common words and patterns")
```

### Project 6: Multiplication Quiz Game

Create `multiplication_quiz.py`:
```python
# multiplication_quiz.py - Timed Multiplication Quiz

import random
import time

print("="*60)
print("      MULTIPLICATION QUIZ GAME")
print("="*60)

# Game settings
print("\n--- DIFFICULTY LEVELS ---")
print("1. Easy (1-5)")
print("2. Medium (1-10)")
print("3. Hard (1-15)")
print("4. Expert (1-20)")

while True:
    difficulty = input("\nSelect difficulty (1-4): ")
    if difficulty in ["1", "2", "3", "4"]:
        break
    print("❌ Please select 1-4")

max_num = {
    "1": 5,
    "2": 10,
    "3": 15,
    "4": 20
}[difficulty]

num_questions = int(input("How many questions? (5-20): "))
num_questions = max(5, min(20, num_questions))  # Clamp between 5-20

print(f"\nGet ready! You'll answer {num_questions} questions.")
input("Press Enter to start...")

# Initialize game
correct = 0
total_time = 0
results = []

# Quiz loop
for question_num in range(1, num_questions + 1):
    # Generate random multiplication
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    correct_answer = num1 * num2
    
    print(f"\n--- Question {question_num}/{num_questions} ---")
    start_time = time.time()
    
    while True:
        try:
            answer = int(input(f"What is {num1} × {num2}? "))
            break
        except ValueError:
            print("❌ Please enter a number!")
    
    end_time = time.time()
    time_taken = end_time - start_time
    total_time += time_taken
    
    if answer == correct_answer:
        print(f"✓ Correct! ({time_taken:.1f}s)")
        correct += 1
        results.append((num1, num2, answer, True, time_taken))
    else:
        print(f"✗ Wrong! The answer is {correct_answer} ({time_taken:.1f}s)")
        results.append((num1, num2, correct_answer, False, time_taken))

# Final results
print("\n" + "="*60)
print("              QUIZ RESULTS")
print("="*60)

# Summary
percentage = (correct / num_questions) * 100
avg_time = total_time / num_questions

print(f"Correct Answers: {correct}/{num_questions}")
print(f"Score: {percentage:.1f}%")
print(f"Total Time: {total_time:.1f} seconds")
print(f"Average Time: {avg_time:.1f} seconds per question")

# Grade
if percentage >= 90:
    grade = "A"
    message = "🌟 Excellent! You're a math wizard!"
elif percentage >= 80:
    grade = "B"
    message = "👍 Great job! Keep practicing!"
elif percentage >= 70:
    grade = "C"
    message = "📚 Good effort! Review your times tables."
elif percentage >= 60:
    grade = "D"
    message = "⚠️ You passed, but need more practice."
else:
    grade = "F"
    message = "❌ Keep studying! Practice makes perfect!"

print(f"\nGrade: {grade}")
print(message)

# Detailed results
show_details = input("\nShow detailed results? (yes/no): ").lower()
if show_details == "yes":
    print("\n--- DETAILED RESULTS ---")
    for i, (n1, n2, ans, correct, t) in enumerate(results, 1):
        status = "✓" if correct else "✗"
        print(f"{i}. {n1} × {n2} = {ans} {status} ({t:.1f}s)")

print("\n" + "="*60)
print("Thanks for playing!")
```

### 📹 Video Resources:

1. **"Nested Loops in Python"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=94UHCEmprCY
   - Duration: 12 minutes
   - Covers: Nested loops, patterns

2. **"Python Projects for Beginners"** by freeCodeCamp
   - Link: https://www.youtube.com/watch?v=8ext9G7xspg
   - Duration: First 40 minutes relevant
   - Covers: Building loop-based projects

### 📚 Text Resources:

1. **Real Python - Python Loops**
   - Link: https://realpython.com/python-for-loop/
   - Comprehensive patterns guide

2. **Programiz - Nested Loops**
   - Link: https://www.programiz.com/python-programming/nested-loops

### ✅ Checkpoint 3:
- [ ] Understand nested loop concept
- [ ] Can create patterns with loops
- [ ] Built at least 3 projects
- [ ] All projects working correctly
- [ ] Code committed to GitHub

---

## 📝 Day 4 Summary & Achievements

### What You Mastered Today:

✅ **for Loops:**
- Basic for loop syntax
- range() function variants
- Iterating over sequences
- Loop patterns and applications

✅ **while Loops:**
- while loop syntax
- Condition-based iteration
- Input validation with loops
- Infinite loop prevention

✅ **Loop Control:**
- break statement (exit loop)
- continue statement (skip iteration)
- pass statement (placeholder)
- Loop else clause

✅ **Nested Loops:**
- Multiple loop levels
- Pattern generation
- Grid/table creation
- Complex iterations

✅ **Projects Completed:**
- Number pyramid generator
- Calculator with menu
- Prime number finder
- Tic-Tac-Toe game
- Password analyzer
- Multiplication quiz

---

## 🎯 Day 4 Assignments

### Mandatory:
- [ ] Complete all practice exercises
- [ ] Build at least 4 of the 6 projects
- [ ] Create 3 different patterns
- [ ] Push all code to GitHub

### Challenge Problems:

**Challenge 1: Hangman Game**
Create a word guessing game:
- Random word from list
- Show blanks for letters
- Track guessed letters
- Allow 6 wrong guesses
- Display hangman ASCII art
- Win/lose conditions

**Challenge 2: Number Pattern Creator**
Create interactive pattern generator:
- Ask user for pattern type
- Ask for size
- Generate: pyramid, diamond, hollow square, etc.
- Allow character choice (*,#,numbers)
- Color coding (bonus)

**Challenge 3: Simple Banking System**
Create menu-based bank system:
- Create account
- Deposit money
- Withdraw money
- Check balance
- View transaction history
- Multiple accounts support

---

## 📊 Self-Assessment Quiz

**Test your understanding:**

1. What will this print?
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```
<details>
<summary>Answer</summary>
0 0
0 1
1 0
1 1
2 0
2 1
</details>

2. What's the difference between break and continue?
<details>
<summary>Answer</summary>
break exits the loop entirely; continue skips to next iteration
</details>

3. What does range(10, 0, -2) produce?
<details>
<summary>Answer</summary>
10, 8, 6, 4, 2 (counting down by 2)
</details>

4. When does the else clause execute in a loop?
<details>
<summary>Answer</summary>
When loop completes normally (no break)
</details>

5. How do you prevent an infinite while loop?
<details>
<summary>Answer</summary>
Ensure condition can become False or use break
</details>

---

## 💡 Loop Best Practices

1. **Choose the Right Loop:**
   - for: Known iterations, sequences
   - while: Unknown iterations, conditions

2. **Avoid Infinite Loops:**
   - Always modify loop variable
   - Ensure condition can become False
   - Use break as safety

3. **Keep It Simple:**
   - Max 2-3 levels of nesting
   - Extract nested loops to functions
   - Use meaningful variable names

4. **Efficiency:**
   - Don't recalculate inside loops
   - Break early when possible
   - Use appropriate range() arguments

5. **Readability:**
```python
# ✅ Good
for student in students:
    print(student.name)

# ❌ Less clear
for i in range(len(students)):
    print(students[i].name)
```

---

## 🐛 Common Loop Mistakes

**Mistake 1: Off-by-One Errors**
```python
# ❌ Wrong - misses last element
for i in range(len(items) - 1):
    print(items[i])

# ✅ Correct
for i in range(len(items)):
    print(items[i])

# ✅ Better
for item in items:
    print(item)
```

**Mistake 2: Modifying List While Iterating**
```python
# ❌ Wrong - unpredictable behavior
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])

# ✅ Correct - iterate over copy
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
```

**Mistake 3: Forgetting to Update Loop Variable**
```python
# ❌ Wrong - infinite loop
i = 0
while i < 10:
    print(i)
    # Forgot: i += 1

# ✅ Correct
i = 0
while i < 10:
    print(i)
    i += 1
```

---

## 🚀 Git Commit & Push

```bash
# Add all files
git add .

# Commit
git commit -m "Day 4: Loops (for/while), nested loops, and 6 projects"

# Push
git push
```

---

## ✅ Day 4 Completion Checklist

### Concepts Mastered:
- [ ] for loop syntax and usage
- [ ] range() function (all forms)
- [ ] while loop syntax
- [ ] break statement
- [ ] continue statement
- [ ] pass statement
- [ ] Loop else clause
- [ ] Nested loops (2+ levels)
- [ ] Pattern generation
- [ ] for vs while decision making

### Projects Completed:
- [ ] Number pyramid (mandatory)
- [ ] Loop calculator (mandatory)
- [ ] Prime finder (mandatory)
- [ ] Tic-Tac-Toe (optional)
- [ ] Password analyzer (optional)
- [ ] Multiplication quiz (optional)
- [ ] At least 1 challenge problem

### Code Quality:
- [ ] Proper indentation
- [ ] No infinite loops
- [ ] Efficient loop design
- [ ] Comments on complex logic
- [ ] Tested thoroughly

### Git & Documentation:
- [ ] All files committed
- [ ] Pushed to GitHub
- [ ] README updated
- [ ] Projects documented

**Overall Completion: ____%**

---

## 📅 Tomorrow's Preview: Day 5

Get ready to learn:
- **Functions:** def keyword
- **Parameters and arguments**
- **Return values**
- **Scope (local vs global)**
- **Lambda functions**

**Preparation:**
- Review all loop concepts
- Practice combining loops with conditionals
- Think about reusable code patterns

---

## 💭 Learning Journal

**Reflection Questions:**

1. Which type of loop do you prefer and why?
   - _______________________

2. What was the most challenging pattern to create?
   - _______________________

3. Rate your understanding of nested loops (1-10):
   - _______________________

4. Which project was most fun to build?
   - _______________________

5. How would you use loops in a real-world project?
   - _______________________

6. Total coding hours today:
   - _______________________

**Tomorrow's Goals:**
- _______________________
- _______________________

---

## 🔗 Complete Resource List

### Official Documentation:
- [Python for Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python while Loops](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Python range() Function](https://docs.python.org/3/library/stdtypes.html#range)

### Video Tutorials:
- [Corey Schafer - Loops](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)
- [Programming with Mosh - Loops](https://www.youtube.com/watch?v=94UHCEmprCY)
- [Tech With Tim - For/While Loops](https://www.youtube.com/watch?v=OnDr4J2UXSA)

### Interactive Learning:
- [W3Schools Python Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [Real Python - Loops](https://realpython.com/python-for-loop/)
- [Programiz - Loops](https://www.programiz.com/python-programming/for-loop)

### Practice Platforms:
- [HackerRank - Loops](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-basic-data-types)
- [Codewars - Loop Kata](https://www.codewars.com/)
- [LeetCode - Loop Problems](https://leetcode.com/problemset/)

---

**Day Status:** Day 4 of 168  
**Previous:** [Day 3 - Conditionals](./Day_03_Complete_Guide.md)  
**Next:** [Day 5 - Functions](./Day_05_Complete_Guide.md)

🎉 **Congratulations on completing Day 4!** You can now create repetitive programs efficiently! 🔄

---

*"Any fool can write code that a computer can understand. Good programmers write code that humans can understand." - Martin Fowler*