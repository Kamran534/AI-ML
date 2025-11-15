# Day 3: Control Flow - Conditional Statements (if/elif/else)

**Duration:** 3-4 hours | **Date:** _________ | **Status:** ⬜ Not Started | ⬜ In Progress | ⬜ Completed

---

## 🎯 Today's Goals

By the end of today, you will:
- ✅ Understand conditional logic and decision making
- ✅ Master if, elif, and else statements
- ✅ Write nested conditional statements
- ✅ Use conditional expressions (ternary operator)
- ✅ Combine conditions with logical operators
- ✅ Build interactive decision-making programs
- ✅ Complete 6+ practical projects

---

## 📋 Pre-Session Checklist

Before starting:
- [ ] Completed Day 1 and Day 2
- [ ] Understand variables and data types
- [ ] Know comparison operators (==, !=, <, >, etc.)
- [ ] Know logical operators (and, or, not)
- [ ] Have Python and VS Code ready
- [ ] Review Boolean logic from Day 2

**Quick Review Test:**
```python
# Can you predict the output?
x = 10
y = 5
print(x > y)        # ?
print(x == 10)      # ?
print(x > 5 and y < 10)  # ?
```

---

## 🕐 Session 1: Introduction to Conditional Statements (45 minutes)

### Part 1.1: The if Statement

**Basic Syntax:**
```python
if condition:
    # Code block to execute if condition is True
    statement1
    statement2
```

**Simple Examples:**
```python
# Example 1: Basic if statement
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This line always executes")

# Example 2: Check if number is positive
number = 10

if number > 0:
    print("The number is positive")

# Example 3: Password check
password = "secret123"

if password == "secret123":
    print("Access granted!")
    print("Welcome to the system")
```

**Important Concepts:**

1. **Indentation Matters:**
```python
# ✅ Correct
if True:
    print("Indented correctly")
    print("Still in the if block")

# ❌ Wrong - IndentationError
if True:
print("This will cause an error")
```

2. **Comparison in Conditions:**
```python
# Different types of conditions
score = 85

if score >= 90:
    print("Excellent!")

if score == 100:
    print("Perfect score!")

if score != 0:
    print("You scored something")

# String comparisons
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")

# Boolean conditions
is_student = True
if is_student:
    print("Student discount applied")

# Checking membership
text = "Python is awesome"
if "Python" in text:
    print("Found Python!")
```

### Part 1.2: The else Statement

**Syntax:**
```python
if condition:
    # Executes if condition is True
    statement1
else:
    # Executes if condition is False
    statement2
```

**Examples:**
```python
# Example 1: Even or Odd
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example 2: Age check
age = 15

if age >= 18:
    print("You can vote")
    print("You are an adult")
else:
    print("You cannot vote yet")
    print("You are a minor")

# Example 3: Password validator
password = input("Enter password: ")

if len(password) >= 8:
    print("Password length is good")
else:
    print("Password must be at least 8 characters")

# Example 4: Temperature check
temp = 25

if temp > 30:
    print("It's hot outside")
else:
    print("Temperature is comfortable")
```

### Part 1.3: The elif Statement

**Syntax:**
```python
if condition1:
    # Executes if condition1 is True
    statement1
elif condition2:
    # Executes if condition1 is False and condition2 is True
    statement2
elif condition3:
    # Executes if condition1 and condition2 are False, condition3 is True
    statement3
else:
    # Executes if all conditions are False
    statement4
```

**Examples:**
```python
# Example 1: Grade calculator
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Example 2: Traffic light
light = "yellow"

if light == "red":
    print("STOP")
elif light == "yellow":
    print("CAUTION - Slow down")
elif light == "green":
    print("GO")
else:
    print("Invalid traffic light color")

# Example 3: BMI categories
bmi = 22.5

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI Category: {category}")

# Example 4: Day of week
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")
```

### Practice Exercise 1: Basic Conditionals

Create `conditionals_practice1.py`:
```python
# conditionals_practice1.py - Basic Conditional Practice

print("=== EXERCISE 1: Number Sign Checker ===")
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("The number is zero")

print("\n=== EXERCISE 2: Age Category ===")
age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"You are a {category}")

print("\n=== EXERCISE 3: Temperature Advisory ===")
temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing! Wear heavy winter clothes")
elif temp < 10:
    print("Cold. Wear a jacket")
elif temp < 20:
    print("Cool. A light jacket might be nice")
elif temp < 30:
    print("Comfortable temperature")
else:
    print("Hot! Stay hydrated")

print("\n=== EXERCISE 4: Discount Calculator ===")
price = float(input("Enter item price: $"))
is_member = input("Are you a member? (yes/no): ").lower()

if is_member == "yes":
    discount = 0.20  # 20% discount
    final_price = price * (1 - discount)
    print(f"Member discount: 20%")
    print(f"Final price: ${final_price:.2f}")
else:
    print(f"No discount applied")
    print(f"Final price: ${price:.2f}")
```

### 📹 Video Resources:

1. **"Python if/elif/else Statements"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=DZwmZ8Usvnk
   - Duration: 10 minutes
   - Covers: Basic conditionals, syntax, examples

2. **"If Statements in Python"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=Zp5MuPOtsSY
   - Duration: 8 minutes
   - Covers: if, else, elif with practical examples

3. **"Python Tutorial: if __name__ == '__main__'"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=sugvnHA7ElY
   - Duration: 7 minutes
   - Advanced concept for later

### 📚 Text Resources:

1. **Python Official Tutorial - Control Flow**
   - Link: https://docs.python.org/3/tutorial/controlflow.html
   - Section 4.1: if Statements

2. **Real Python - Conditional Statements**
   - Link: https://realpython.com/python-conditional-statements/
   - Comprehensive guide with examples

3. **W3Schools - Python If...Else**
   - Link: https://www.w3schools.com/python/python_conditions.asp
   - Quick reference with try-it-yourself examples

### ✅ Checkpoint 1:
- [ ] Understand if statement syntax
- [ ] Can write if-else statements
- [ ] Know how to use elif
- [ ] Understand indentation importance
- [ ] Completed basic practice exercises

---

## 🕑 Session 2: Complex Conditions & Nested Statements (60 minutes)

### Part 2.1: Multiple Conditions with Logical Operators

**Using AND:**
```python
# Example 1: Loan eligibility
age = 30
income = 50000
credit_score = 700

if age >= 21 and income >= 30000 and credit_score >= 650:
    print("Loan approved!")
else:
    print("Loan denied")

# Example 2: Working hours
day = "Monday"
time = 14  # 2 PM

if day != "Saturday" and day != "Sunday" and time >= 9 and time <= 17:
    print("Office is open")
else:
    print("Office is closed")

# Example 3: Valid password
password = "SecurePass123"
has_length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)

if has_length and has_upper and has_digit:
    print("Password is strong")
else:
    print("Password is weak")
```

**Using OR:**
```python
# Example 1: Weekend check
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")

# Example 2: Emergency contact
relationship = "parent"

if relationship == "parent" or relationship == "spouse" or relationship == "sibling":
    print("Valid emergency contact")
else:
    print("Please provide a closer relationship")

# Example 3: VIP access
is_premium = False
is_admin = True

if is_premium or is_admin:
    print("Access granted to VIP section")
else:
    print("Upgrade to premium for access")
```

**Combining AND and OR:**
```python
# Example 1: Ticket pricing
age = 25
is_student = True
is_senior = False

if (age < 18 or age > 65) or is_student:
    print("Discounted ticket: $5")
else:
    print("Regular ticket: $10")

# Example 2: Access control
time = 20  # 8 PM
is_employee = True
has_keycard = True

if (time >= 9 and time <= 17) or (is_employee and has_keycard):
    print("Access granted")
else:
    print("Access denied")

# Example 3: Flight booking
destination = "Paris"
budget = 1000
has_passport = True

if destination in ["Paris", "London", "Rome"] and budget >= 800 and has_passport:
    print("Booking confirmed!")
else:
    print("Cannot complete booking")
    if not has_passport:
        print("Reason: Passport required")
    elif budget < 800:
        print("Reason: Insufficient budget")
```

### Part 2.2: Nested if Statements

**Basic Nesting:**
```python
# Example 1: Age and license check
age = 25
has_license = True

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can drive!")
    else:
        print("But you need a license first")
else:
    print("You are too young to drive")

# Example 2: Login system
username = "admin"
password = "pass123"

if username == "admin":
    print("Username correct")
    if password == "pass123":
        print("Login successful!")
        print("Welcome to the admin panel")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Example 3: Scholarship eligibility
gpa = 3.8
income = 25000
activities = 5

if gpa >= 3.5:
    print("GPA requirement met")
    if income < 30000:
        print("Income requirement met")
        if activities >= 3:
            print("🎉 Scholarship awarded!")
        else:
            print("Need more extracurricular activities")
    else:
        print("Income too high for need-based scholarship")
else:
    print("GPA requirement not met")
```

**Complex Nesting:**
```python
# Example: Movie ticket pricing
age = 15
day = "Tuesday"
is_student = True

if age < 12:
    price = 5
    print("Child ticket")
elif age >= 65:
    price = 6
    print("Senior ticket")
else:
    # Regular adult pricing
    if day == "Tuesday":
        price = 7
        print("Tuesday discount")
    elif is_student:
        price = 8
        print("Student discount")
    else:
        price = 12
        print("Regular ticket")

print(f"Ticket price: ${price}")

# Example: Grade with honors
score = 95
attendance = 98

if score >= 90:
    if attendance >= 95:
        print("A+ with Honors")
    else:
        print("A")
elif score >= 80:
    if attendance >= 90:
        print("B with Good Attendance")
    else:
        print("B")
elif score >= 70:
    print("C")
else:
    print("Need to improve")
```

### Part 2.3: Conditional Expressions (Ternary Operator)

**Basic Syntax:**
```python
# Syntax: value_if_true if condition else value_if_false

# Example 1: Simple assignment
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# Example 2: Even or odd
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

# Example 3: Max of two numbers
a = 10
b = 15
maximum = a if a > b else b
print(f"Maximum: {maximum}")

# Example 4: Discount
price = 100
is_member = True
final_price = price * 0.9 if is_member else price
print(f"Final price: ${final_price}")
```

**Nested Ternary (Use Sparingly):**
```python
# Example: Grade assignment
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")

# Better to use regular if-elif for readability:
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Practice Exercise 2: Complex Conditionals

Create `conditionals_practice2.py`:
```python
# conditionals_practice2.py - Complex Conditional Practice

print("=== EXERCISE 1: Restaurant Reservation ===")
party_size = int(input("Party size: "))
time = int(input("Time (24-hour format): "))
has_reservation = input("Do you have a reservation? (yes/no): ").lower()

if party_size <= 4:
    if time >= 17 and time <= 22:
        if has_reservation == "yes":
            print("✓ Table confirmed!")
            print("Please arrive 10 minutes early")
        else:
            print("Walk-ins available, 15-minute wait")
    else:
        print("We're only open 5 PM - 10 PM")
else:
    if has_reservation == "yes":
        print("✓ Large party reservation confirmed")
        print("Please contact us to confirm details")
    else:
        print("Parties over 4 require reservation")
        print("Please call to book")

print("\n=== EXERCISE 2: Tax Calculator ===")
income = float(input("Annual income: $"))
filing_status = input("Filing status (single/married): ").lower()

if filing_status == "single":
    if income <= 10000:
        tax_rate = 0.10
    elif income <= 40000:
        tax_rate = 0.12
    elif income <= 85000:
        tax_rate = 0.22
    else:
        tax_rate = 0.24
elif filing_status == "married":
    if income <= 20000:
        tax_rate = 0.10
    elif income <= 80000:
        tax_rate = 0.12
    elif income <= 170000:
        tax_rate = 0.22
    else:
        tax_rate = 0.24
else:
    print("Invalid filing status")
    tax_rate = 0

tax_amount = income * tax_rate
print(f"\nTax rate: {tax_rate*100}%")
print(f"Tax amount: ${tax_amount:,.2f}")
print(f"After-tax income: ${income - tax_amount:,.2f}")

print("\n=== EXERCISE 3: Shipping Calculator ===")
weight = float(input("Package weight (kg): "))
destination = input("Destination (domestic/international): ").lower()
is_express = input("Express shipping? (yes/no): ").lower() == "yes"

if destination == "domestic":
    base_rate = 5
    per_kg = 2
elif destination == "international":
    base_rate = 15
    per_kg = 5
else:
    print("Invalid destination")
    base_rate = 0
    per_kg = 0

shipping_cost = base_rate + (weight * per_kg)

if is_express:
    shipping_cost *= 1.5
    print("Express shipping selected")

print(f"\nShipping cost: ${shipping_cost:.2f}")

if shipping_cost > 50:
    print("Free insurance included!")
```

### 📹 Video Resources:

1. **"Python Nested If Statements"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=42MBMSOJgj4
   - Duration: 8 minutes
   - Covers: Nested conditions, complex logic

2. **"Python Logical Operators"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=DZwmZ8Usvnk
   - Duration: 10 minutes
   - Covers: and, or, not in conditions

3. **"Ternary Operator in Python"** by Real Python
   - Link: https://realpython.com/python-conditional-expressions/
   - Text tutorial with examples

### 📚 Text Resources:

1. **Python Docs - More Control Flow Tools**
   - Link: https://docs.python.org/3/tutorial/controlflow.html#if-statements

2. **Real Python - Complex Conditionals**
   - Link: https://realpython.com/python-conditional-statements/

### ✅ Checkpoint 2:
- [ ] Can combine conditions with and/or
- [ ] Understand nested if statements
- [ ] Know when to use ternary operator
- [ ] Can write complex decision logic
- [ ] Completed complex practice exercises

---

## 🕒 Session 3: Practical Applications & Projects (90 minutes)

### Project 1: Grade Calculator

Create `grade_calculator.py`:
```python
# grade_calculator.py - Comprehensive Grade Calculator

print("="*50)
print("     STUDENT GRADE CALCULATOR")
print("="*50)

# Get student information
student_name = input("\nStudent Name: ")

# Get scores
print("\nEnter scores for each assignment:")
homework1 = float(input("Homework 1 (out of 100): "))
homework2 = float(input("Homework 2 (out of 100): "))
homework3 = float(input("Homework 3 (out of 100): "))
midterm = float(input("Midterm Exam (out of 100): "))
final = float(input("Final Exam (out of 100): "))
participation = float(input("Participation (out of 100): "))

# Calculate weighted average
# Weights: Homework 30%, Midterm 25%, Final 35%, Participation 10%
homework_avg = (homework1 + homework2 + homework3) / 3
final_score = (homework_avg * 0.30 + 
               midterm * 0.25 + 
               final * 0.35 + 
               participation * 0.10)

# Determine letter grade
if final_score >= 93:
    letter_grade = "A"
    gpa = 4.0
elif final_score >= 90:
    letter_grade = "A-"
    gpa = 3.7
elif final_score >= 87:
    letter_grade = "B+"
    gpa = 3.3
elif final_score >= 83:
    letter_grade = "B"
    gpa = 3.0
elif final_score >= 80:
    letter_grade = "B-"
    gpa = 2.7
elif final_score >= 77:
    letter_grade = "C+"
    gpa = 2.3
elif final_score >= 73:
    letter_grade = "C"
    gpa = 2.0
elif final_score >= 70:
    letter_grade = "C-"
    gpa = 1.7
elif final_score >= 67:
    letter_grade = "D+"
    gpa = 1.3
elif final_score >= 63:
    letter_grade = "D"
    gpa = 1.0
elif final_score >= 60:
    letter_grade = "D-"
    gpa = 0.7
else:
    letter_grade = "F"
    gpa = 0.0

# Determine if honors
honors = ""
if final_score >= 90 and participation >= 85:
    honors = "with Honors"
elif final_score >= 85 and participation >= 90:
    honors = "with High Participation"

# Display report card
print("\n" + "="*50)
print("           GRADE REPORT CARD")
print("="*50)
print(f"Student: {student_name}")
print("-"*50)
print("ASSIGNMENT SCORES:")
print(f"  Homework 1:       {homework1:>6.2f}")
print(f"  Homework 2:       {homework2:>6.2f}")
print(f"  Homework 3:       {homework3:>6.2f}")
print(f"  Homework Average: {homework_avg:>6.2f}")
print(f"  Midterm Exam:     {midterm:>6.2f}")
print(f"  Final Exam:       {final:>6.2f}")
print(f"  Participation:    {participation:>6.2f}")
print("-"*50)
print(f"FINAL SCORE:        {final_score:>6.2f}")
print(f"LETTER GRADE:       {letter_grade} {honors}")
print(f"GPA:                {gpa:.2f}")
print("="*50)

# Additional feedback
if final_score >= 90:
    print("🌟 Excellent work! Keep it up!")
elif final_score >= 80:
    print("👍 Good job! You're doing well.")
elif final_score >= 70:
    print("📚 Passing grade. Consider studying more.")
elif final_score >= 60:
    print("⚠️  Barely passing. Please seek help.")
else:
    print("❌ Failing grade. Please meet with instructor.")

# Show what's needed to improve
if letter_grade != "A":
    points_to_A = 93 - final_score
    print(f"\nYou need {points_to_A:.2f} more points for an A")
```

### Project 2: ATM Machine Simulator

Create `atm_simulator.py`:
```python
# atm_simulator.py - ATM Machine Simulator

print("="*50)
print("        WELCOME TO PYTHON BANK ATM")
print("="*50)

# Account setup
account_balance = 1000.00
pin = "1234"
daily_withdrawal_limit = 500.00
total_withdrawn_today = 0.00

# PIN verification
print("\nPlease enter your PIN:")
user_pin = input("PIN: ")

if user_pin == pin:
    print("\n✓ PIN Accepted")
    
    # Main ATM menu loop (we'll use a simple if-elif for now)
    while True:
        print("\n" + "="*50)
        print("           ATM MAIN MENU")
        print("="*50)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        print("="*50)
        
        choice = input("\nSelect option (1-4): ")
        
        if choice == "1":
            # Check Balance
            print("\n" + "-"*50)
            print(f"Current Balance: ${account_balance:,.2f}")
            print("-"*50)
            
        elif choice == "2":
            # Withdraw Money
            print("\n--- WITHDRAWAL ---")
            print(f"Available balance: ${account_balance:,.2f}")
            print(f"Daily limit remaining: ${daily_withdrawal_limit - total_withdrawn_today:,.2f}")
            
            amount = float(input("Enter amount to withdraw: $"))
            
            if amount <= 0:
                print("❌ Invalid amount!")
            elif amount > account_balance:
                print("❌ Insufficient funds!")
                print(f"Your balance is only ${account_balance:,.2f}")
            elif total_withdrawn_today + amount > daily_withdrawal_limit:
                print("❌ Daily withdrawal limit exceeded!")
                remaining = daily_withdrawal_limit - total_withdrawn_today
                print(f"You can only withdraw ${remaining:,.2f} more today")
            else:
                account_balance -= amount
                total_withdrawn_today += amount
                print(f"\n✓ Withdrawal successful!")
                print(f"Amount withdrawn: ${amount:,.2f}")
                print(f"New balance: ${account_balance:,.2f}")
                
        elif choice == "3":
            # Deposit Money
            print("\n--- DEPOSIT ---")
            amount = float(input("Enter amount to deposit: $"))
            
            if amount <= 0:
                print("❌ Invalid amount!")
            elif amount > 10000:
                print("❌ Deposits over $10,000 require teller assistance")
            else:
                account_balance += amount
                print(f"\n✓ Deposit successful!")
                print(f"Amount deposited: ${amount:,.2f}")
                print(f"New balance: ${account_balance:,.2f}")
                
        elif choice == "4":
            # Exit
            print("\n" + "="*50)
            print("Thank you for using Python Bank ATM")
            print(f"Final balance: ${account_balance:,.2f}")
            print("="*50)
            break
            
        else:
            print("❌ Invalid option. Please select 1-4")
            
else:
    print("\n❌ Incorrect PIN")
    print("Access denied. Card retained.")
```

### Project 3: Quiz Game

Create `quiz_game.py`:
```python
# quiz_game.py - Interactive Quiz Game

print("="*60)
print("           PYTHON PROGRAMMING QUIZ")
print("="*60)
print("\nAnswer the following questions. Good luck!\n")

score = 0
total_questions = 5

# Question 1
print("Question 1: What is the result of 10 // 3?")
print("A) 3.33")
print("B) 3")
print("C) 4")
print("D) 3.0")
answer1 = input("Your answer (A/B/C/D): ").upper()

if answer1 == "B":
    print("✓ Correct!\n")
    score += 1
else:
    print("✗ Wrong! The answer is B) 3\n")

# Question 2
print("Question 2: Which operator is used for exponentiation?")
print("A) ^")
print("B) **")
print("C) //")
print("D) %")
answer2 = input("Your answer (A/B/C/D): ").upper()

if answer2 == "B":
    print("✓ Correct!\n")
    score += 1
else:
    print("✗ Wrong! The answer is B) **\n")

# Question 3
print("Question 3: What does the len() function do?")
print("A) Returns the length of a string")
print("B) Returns the type of variable")
print("C) Converts to lowercase")
print("D) Rounds a number")
answer3 = input("Your answer (A/B/C/D): ").upper()

if answer3 == "A":
    print("✓ Correct!\n")
    score += 1
else:
    print("✗ Wrong! The answer is A) Returns the length of a string\n")

# Question 4
print("Question 4: What is the output of: bool(0)?")
print("A) True")
print("B) False")
print("C) 0")
print("D) Error")
answer4 = input("Your answer (A/B/C/D): ").upper()

if answer4 == "B":
    print("✓ Correct!\n")
    score += 1
else:
    print("✗ Wrong! The answer is B) False\n")

# Question 5
print("Question 5: Which is the correct way to comment in Python?")
print("A) // comment")
print("B) /* comment */")
print("C) # comment")
print("D) <!-- comment -->")
answer5 = input("Your answer (A/B/C/D): ").upper()

if answer5 == "C":
    print("✓ Correct!\n")
    score += 1
else:
    print("✗ Wrong! The answer is C) # comment\n")

# Calculate percentage
percentage = (score / total_questions) * 100

# Display results
print("="*60)
print("                QUIZ RESULTS")
print("="*60)
print(f"Correct Answers: {score}/{total_questions}")
print(f"Score: {percentage:.1f}%")

# Determine grade
if percentage >= 90:
    grade = "A"
    message = "🌟 Excellent! You're a Python star!"
elif percentage >= 80:
    grade = "B"
    message = "👍 Great job! Keep learning!"
elif percentage >= 70:
    grade = "C"
    message = "📚 Good effort! Review the concepts."
elif percentage >= 60:
    grade = "D"
    message = "⚠️  You passed, but need more practice."
else:
    grade = "F"
    message = "❌ Keep studying! You'll get there!"

print(f"Grade: {grade}")
print(message)
print("="*60)
```

### Project 4: Restaurant Order System

Create `restaurant_order.py`:
```python
# restaurant_order.py - Restaurant Ordering System

print("="*60)
print("      WELCOME TO PYTHON RESTAURANT")
print("="*60)

# Menu
print("\n--- MENU ---")
print("BURGERS:")
print("  1. Classic Burger      $8.99")
print("  2. Cheese Burger       $9.99")
print("  3. Deluxe Burger       $12.99")
print("\nSIDES:")
print("  4. French Fries        $3.99")
print("  5. Onion Rings         $4.99")
print("  6. Salad               $5.99")
print("\nDRINKS:")
print("  7. Soda                $1.99")
print("  8. Juice               $2.99")
print("  9. Water               Free")
print("\nDESSERTS:")
print("  10. Ice Cream          $4.99")
print("  11. Cake               $5.99")

# Initialize order
total = 0.0
items = []

# Get customer info
name = input("\nYour name: ")
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

# Order items
print("\nEnter item numbers (0 to finish):")

while True:
    item = input("Item number: ")
    
    if item == "0":
        break
    elif item == "1":
        items.append("Classic Burger")
        total += 8.99
    elif item == "2":
        items.append("Cheese Burger")
        total += 9.99
    elif item == "3":
        items.append("Deluxe Burger")
        total += 12.99
    elif item == "4":
        items.append("French Fries")
        total += 3.99
    elif item == "5":
        items.append("Onion Rings")
        total += 4.99
    elif item == "6":
        items.append("Salad")
        total += 5.99
    elif item == "7":
        items.append("Soda")
        total += 1.99
    elif item == "8":
        items.append("Juice")
        total += 2.99
    elif item == "9":
        items.append("Water")
        # Water is free
    elif item == "10":
        items.append("Ice Cream")
        total += 4.99
    elif item == "11":
        items.append("Cake")
        total += 5.99
    else:
        print("Invalid item number!")
        continue
    
    print(f"Added: {items[-1]}")

# Check if order has items
if len(items) == 0:
    print("\nNo items ordered. Thank you!")
else:
    # Calculate discounts
    subtotal = total
    discount = 0
    
    # Member discount
    if is_member:
        discount = subtotal * 0.10
        print(f"\n✓ Member discount applied: 10%")
    
    # Large order discount
    if subtotal > 50:
        additional_discount = subtotal * 0.05
        discount += additional_discount
        print(f"✓ Large order discount: 5%")
    
    # Calculate tax
    tax = (subtotal - discount) * 0.08
    
    # Final total
    final_total = subtotal - discount + tax
    
    # Generate receipt
    print("\n" + "="*60)
    print("                  RECEIPT")
    print("="*60)
    print(f"Customer: {name}")
    if is_member:
        print("Member: Yes ⭐")
    print("-"*60)
    print("ITEMS:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")
    print("-"*60)
    print(f"Subtotal:           ${subtotal:>8.2f}")
    if discount > 0:
        print(f"Discount:          -${discount:>8.2f}")
    print(f"Tax (8%):           ${tax:>8.2f}")
    print("="*60)
    print(f"TOTAL:              ${final_total:>8.2f}")
    print("="*60)
    
    # Payment
    print("\nHow would you like to pay?")
    print("1. Cash")
    print("2. Credit Card")
    print("3. Debit Card")
    payment_method = input("Select (1-3): ")
    
    if payment_method == "1":
        cash = float(input(f"Enter cash amount: $"))
        if cash >= final_total:
            change = cash - final_total
            print(f"\nPayment received: ${cash:.2f}")
            print(f"Change: ${change:.2f}")
            print("\n✓ Order complete! Thank you!")
        else:
            print(f"\nInsufficient cash. ${final_total - cash:.2f} short.")
    elif payment_method == "2" or payment_method == "3":
        card_type = "Credit Card" if payment_method == "2" else "Debit Card"
        print(f"\n{card_type} payment processing...")
        print("✓ Payment approved!")
        print("✓ Order complete! Thank you!")
    else:
        print("\nInvalid payment method.")
    
    # Estimated wait time
    item_count = len(items)
    if item_count <= 2:
        wait_time = "5-10 minutes"
    elif item_count <= 5:
        wait_time = "10-15 minutes"
    else:
        wait_time = "15-20 minutes"
    
    print(f"\nEstimated wait time: {wait_time}")
    print("Your order number is: #42")
```

### Project 5: Simple Adventure Game

Create `adventure_game.py`:
```python
# adventure_game.py - Text-Based Adventure Game

print("="*60)
print("         THE PYTHON ADVENTURE")
print("="*60)
print("\nYou wake up in a mysterious forest...")
print("Your goal is to find your way home.")

# Game state
health = 100
has_sword = False
has_key = False
gold = 0

# Introduction
name = input("\nWhat is your name, adventurer? ")
print(f"\nWelcome, {name}!")

# Scene 1: The Fork
print("\n" + "-"*60)
print("SCENE 1: The Fork in the Road")
print("-"*60)
print("You come to a fork in the road.")
print("To the LEFT, you see a dark cave.")
print("To the RIGHT, you see a small village.")
print("STRAIGHT ahead is a mysterious castle.")

choice1 = input("\nWhich way do you go? (left/right/straight): ").lower()

if choice1 == "left":
    # Cave path
    print("\n--- THE CAVE ---")
    print("You enter the dark cave...")
    print("You find a rusty sword!")
    has_sword = True
    print("✓ Sword added to inventory")
    
    print("\nDeeper in the cave, you encounter a sleeping dragon!")
    action = input("Do you (fight/sneak/run)? ").lower()
    
    if action == "fight":
        if has_sword:
            print("\nYou bravely fight the dragon with your sword!")
            print("After an epic battle, you defeat the dragon!")
            gold += 100
            print("✓ You found 100 gold!")
        else:
            print("\nYou have no weapon! The dragon attacks!")
            health -= 50
            print(f"⚠️  Health: {health}/100")
    elif action == "sneak":
        print("\nYou carefully sneak past the sleeping dragon...")
        print("✓ You escape safely!")
        gold += 20
        print("You find 20 gold on the ground!")
    else:
        print("\nYou run away from the cave.")
        
elif choice1 == "right":
    # Village path
    print("\n--- THE VILLAGE ---")
    print("You arrive at a peaceful village.")
    print("An old merchant approaches you.")
    print("'I have a magical key for sale - 50 gold'")
    
    if gold >= 50:
        buy = input("Do you buy the key? (yes/no): ").lower()
        if buy == "yes":
            gold -= 50
            has_key = True
            print("✓ Key purchased!")
    else:
        print("You don't have enough gold.")
    
    print("\nA healer offers to restore your health for 30 gold.")
    if gold >= 30:
        heal = input("Do you accept? (yes/no): ").lower()
        if heal == "yes":
            gold -= 30
            health = 100
            print("✓ Health restored to 100!")
            
else:
    # Castle path
    print("\n--- THE CASTLE ---")
    print("You approach the mysterious castle.")
    print("The gate is locked!")
    
    if has_key:
        print("\nYou use the magical key to open the gate!")
        print("Inside, you find a treasure chest with 200 gold!")
        gold += 200
    else:
        print("\nYou need a key to enter.")
        print("You must find another way.")

# Final scene
print("\n" + "="*60)
print("            GAME OVER")
print("="*60)
print(f"Adventurer: {name}")
print(f"Final Health: {health}/100")
print(f"Gold Collected: {gold}")
print(f"Sword: {'Yes ⚔️' if has_sword else 'No'}")
print(f"Key: {'Yes 🔑' if has_key else 'No'}")

# Determine ending
if health > 80 and gold >= 100:
    print("\n🏆 PERFECT ENDING!")
    print("You successfully navigated the adventure and returned home wealthy!")
elif health > 50:
    print("\n✓ GOOD ENDING!")
    print("You made it home safely!")
elif health > 0:
    print("\n⚠️  SURVIVED!")
    print("You barely made it home alive.")
else:
    print("\n❌ GAME OVER!")
    print("You didn't survive the adventure.")

print("="*60)
```

### 📹 Video Resources:

1. **"Building Projects with Python"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=DLn3jOsNRVE
   - Duration: 20+ minutes
   - Covers: Project structure, logic flow

2. **"Python Mini Projects"** by freeCodeCamp
   - Link: https://www.youtube.com/watch?v=8ext9G7xspg
   - Duration: 2+ hours (watch first 30 mins)
   - Covers: Multiple beginner projects

### 📚 Text Resources:

1. **Real Python - Building Projects**
   - Link: https://realpython.com/tutorials/projects/
   - Various beginner to advanced projects

2. **Automate the Boring Stuff - Projects**
   - Link: https://automatetheboringstuff.com/
   - Practical projects with explanations

### ✅ Checkpoint 3:
- [ ] Built grade calculator
- [ ] Created ATM simulator
- [ ] Made quiz game
- [ ] Developed restaurant order system
- [ ] Coded adventure game
- [ ] All projects working correctly

---

## 📝 Day 3 Summary & Achievements

### What You Mastered Today:

✅ **Conditional Statements:**
- if, elif, else syntax
- Indentation rules
- Multiple elif chains

✅ **Complex Logic:**
- Combining conditions with and/or/not
- Nested if statements
- Conditional expressions (ternary)

✅ **Practical Applications:**
- Decision-making programs
- User input validation
- Game logic
- Business logic (pricing, grading)

✅ **Projects Completed:**
- Grade calculator with honors
- ATM machine simulator
- Interactive quiz game
- Restaurant ordering system
- Text adventure game

---

## 🎯 Day 3 Assignments

### Mandatory:
- [ ] Complete all practice exercises
- [ ] Build at least 3 of the 5 projects
- [ ] Test all edge cases
- [ ] Push to GitHub

### Challenge Problems:

**Challenge 1: Rock Paper Scissors Game**
Create a game where:
- Player chooses rock, paper, or scissors
- Computer makes random choice
- Determine winner
- Keep score over multiple rounds
- Display statistics

**Challenge 2: Loan Calculator**
Create a program that:
- Gets loan amount, interest rate, years
- Calculates monthly payment
- Shows amortization summary
- Determines if user qualifies based on income
- Suggests better loan terms

**Challenge 3: Password Generator**
Create a tool that:
- Asks user for password requirements
- Length (8-32 characters)
- Include uppercase? (yes/no)
- Include numbers? (yes/no)
- Include symbols? (yes/no)
- Generates password based on criteria
- Rates password strength

---

## 📊 Self-Assessment Quiz

**Test your understanding:**

1. What's wrong with this code?
```python
if x > 10
    print("Greater than 10")
```
<details>
<summary>Answer</summary>
Missing colon after condition: if x > 10:
</details>

2. What will this print?
```python
x = 15
if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
else:
    print("D")
```
<details>
<summary>Answer</summary>
B (first true condition is x > 10)
</details>

3. What's the output?
```python
age = 25
status = "Adult" if age >= 18 else "Minor"
print(status)
```
<details>
<summary>Answer</summary>
Adult
</details>

4. True or False: You can have multiple elif statements.
<details>
<summary>Answer</summary>
True - you can have as many as needed
</details>

5. What's the output?
```python
x = 10
if x > 5 and x < 15:
    print("Yes")
else:
    print("No")
```
<details>
<summary>Answer</summary>
Yes (both conditions are true)
</details>

---

## 💡 Best Practices Learned

1. **Indentation Consistency**
   - Use 4 spaces (Python standard)
   - Don't mix tabs and spaces

2. **Clear Conditions**
   - Use parentheses for clarity: `if (a > 5) and (b < 10):`
   - Break complex conditions into variables

3. **Order Matters**
   - Put most specific conditions first
   - Else should be the catch-all

4. **Avoid Deep Nesting**
   - Max 2-3 levels of nesting
   - Consider refactoring if deeper

5. **Use elif, Not Multiple ifs**
   - More efficient (stops at first True)
   - Clearer logic flow

---

## 🐛 Common Mistakes & Solutions

**Mistake 1: Forgetting Colon**
```python
# ❌ Wrong
if x > 10
    print("Error")

# ✅ Correct
if x > 10:
    print("Correct")
```

**Mistake 2: Wrong Indentation**
```python
# ❌ Wrong
if x > 10:
print("Error")

# ✅ Correct
if x > 10:
    print("Correct")
```

**Mistake 3: Using = Instead of ==**
```python
# ❌ Wrong (assignment, not comparison)
if x = 10:
    print("Error")

# ✅ Correct
if x == 10:
    print("Correct")
```

**Mistake 4: Unreachable Code**
```python
# ❌ Wrong - second condition never checked
if x > 5:
    print("Greater than 5")
if x > 10:  # Should be elif
    print("Greater than 10")

# ✅ Correct
if x > 5:
    print("Greater than 5")
elif x > 10:
    print("Greater than 10")
```

---

## 🚀 Git Commit & Push

```bash
# Add all new files
git add .

# Commit with descriptive message
git commit -m "Day 3: Conditional statements and decision-making projects"

# Push to GitHub
git push

# Or if first time pushing this branch
git push -u origin main
```

---

## ✅ Day 3 Completion Checklist

### Concepts Mastered:
- [ ] if statement syntax
- [ ] if-else statements
- [ ] elif chains
- [ ] Nested conditionals
- [ ] Logical operators in conditions
- [ ] Conditional expressions (ternary)
- [ ] Input validation
- [ ] Complex decision logic

### Projects Completed:
- [ ] Grade calculator (mandatory)
- [ ] ATM simulator (mandatory)
- [ ] Quiz game (mandatory)
- [ ] Restaurant order system (optional)
- [ ] Adventure game (optional)
- [ ] At least 1 challenge problem

### Code Quality:
- [ ] Proper indentation
- [ ] Meaningful variable names
- [ ] Comments explaining logic
- [ ] Tested with different inputs
- [ ] No syntax errors

### Git & Documentation:
- [ ] All files committed
- [ ] Pushed to GitHub
- [ ] README updated
- [ ] Code documented

**Overall Completion: ____%**

---

## 📅 Tomorrow's Preview: Day 4

Get ready to learn:
- **Loops:** for and while loops
- **Iteration** over sequences
- **Loop control:** break, continue
- **Nested loops**
- **Building repetitive programs**

**Preparation:**
- Review conditional statements
- Understand range() function
- Be ready to combine conditions with loops

---

## 💭 Learning Journal

**Reflection Questions:**

1. What type of conditional logic did you find most useful?
   - _______________________

2. Which project was most challenging?
   - _______________________

3. Rate your understanding of nested if statements (1-10):
   - _______________________

4. How would you use conditionals in a real project?
   - _______________________

5. What was your biggest "aha!" moment today?
   - _______________________

6. How many hours did you code today?
   - _______________________

**Tomorrow's Goals:**
- _______________________
- _______________________

---

## 🔗 Complete Resource List

### Official Documentation:
- [Python if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

### Video Tutorials:
- [Corey Schafer - Conditionals](https://www.youtube.com/watch?v=DZwmZ8Usvnk)
- [Programming with Mosh - If Statements](https://www.youtube.com/watch?v=Zp5MuPOtsSY)
- [Tech With Tim - Python Conditionals](https://www.youtube.com/watch?v=42MBMSOJgj4)

### Interactive Learning:
- [W3Schools Python Conditions](https://www.w3schools.com/python/python_conditions.asp)
- [Real Python - Conditionals](https://realpython.com/python-conditional-statements/)
- [Python Tutor](https://pythontutor.com/)

### Practice Platforms:
- [HackerRank - Conditionals](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-conditionals)
- [Codewars](https://www.codewars.com/)
- [LeetCode Easy Problems](https://leetcode.com/problemset/)

---

**Day Status:** Day 3 of 168  
**Previous:** [Day 2 - Data Types & Operators](./Day_02_Complete_Guide.md)  
**Next:** [Day 4 - Loops](./Day_04_Complete_Guide.md)

🎉 **Congratulations on completing Day 3!** You can now make decisions in code! 🚀

---

*"Code is like humor. When you have to explain it, it's bad." - Cory House*