# Day 6: Lists & Tuples - Data Structures

**Duration:** 3-4 hours | **Date:** _________ | **Status:** ⬜ Not Started | ⬜ In Progress | ⬜ Completed

---

## 🎯 Today's Goals

By the end of today, you will:
- ✅ Understand lists and how to use them
- ✅ Master list operations and methods
- ✅ Create and manipulate tuples
- ✅ Use list comprehensions
- ✅ Sort and search lists efficiently
- ✅ Understand list vs tuple differences
- ✅ Build data-driven applications

---

## 📋 Pre-Session Checklist

Before starting:
- [ ] Completed Days 1-5
- [ ] Understand variables and data types
- [ ] Comfortable with loops
- [ ] Can write functions
- [ ] Have Python and VS Code ready

**Quick Review Test:**
```python
# Can you predict what this does?
numbers = [1, 2, 3, 4, 5]
print(numbers[0])    # ?
print(numbers[-1])   # ?
print(len(numbers))  # ?
```

---

## 🕐 Session 1: Introduction to Lists (60 minutes)

### Part 1.1: What are Lists?

**Definition:**
A list is an ordered, mutable (changeable) collection of items.

**Why Use Lists?**
- Store multiple values in one variable
- Organize related data
- Process collections of items
- Build dynamic data structures

**Creating Lists:**
```python
# Empty list
empty_list = []

# List with numbers
numbers = [1, 2, 3, 4, 5]

# List with strings
fruits = ["apple", "banana", "cherry"]

# List with mixed types
mixed = [1, "hello", 3.14, True]

# List with lists (nested)
nested = [[1, 2], [3, 4], [5, 6]]

# Using list() constructor
letters = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
```

### Part 1.2: Accessing List Elements

**Indexing (starts at 0):**
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing
print(fruits[0])   # apple (first element)
print(fruits[1])   # banana
print(fruits[2])   # cherry
print(fruits[4])   # elderberry (last element)

# Negative indexing (from end)
print(fruits[-1])  # elderberry (last)
print(fruits[-2])  # date (second from last)
print(fruits[-5])  # apple (first)

# Get length
print(len(fruits))  # 5

# Check if item exists
print("banana" in fruits)      # True
print("grape" in fruits)       # False
print("grape" not in fruits)   # True
```

**Slicing:**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end]
print(numbers[2:5])    # [2, 3, 4] (end not included)
print(numbers[0:3])    # [0, 1, 2]
print(numbers[5:8])    # [5, 6, 7]

# Shortcuts
print(numbers[:4])     # [0, 1, 2, 3] (from start to 4)
print(numbers[6:])     # [6, 7, 8, 9] (from 6 to end)
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (full copy)

# With step [start:end:step]
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (odd numbers)
print(numbers[::3])    # [0, 3, 6, 9] (every 3rd)

# Reverse
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Complex slicing
print(numbers[2:8:2])  # [2, 4, 6]
print(numbers[7:2:-1]) # [7, 6, 5, 4, 3]
```

### Part 1.3: Modifying Lists

**Changing Elements:**
```python
fruits = ["apple", "banana", "cherry"]

# Change single element
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Change multiple elements
fruits[0:2] = ["avocado", "apricot"]
print(fruits)  # ['avocado', 'apricot', 'cherry']

# Replace with different length
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30, 40]
print(numbers)  # [1, 20, 30, 40, 4, 5]
```

**Adding Elements:**
```python
fruits = ["apple", "banana"]

# append() - add to end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert() - add at specific position
fruits.insert(1, "blueberry")  # insert at index 1
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']

# extend() - add multiple items
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# Using + operator
more_fruits = fruits + ["fig", "grape"]
print(more_fruits)

# Using * operator (repeat)
repeat = ["hi"] * 3
print(repeat)  # ['hi', 'hi', 'hi']
```

**Removing Elements:**
```python
fruits = ["apple", "banana", "cherry", "date", "banana"]

# remove() - remove first occurrence
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'date', 'banana']

# pop() - remove and return last item
last = fruits.pop()
print(last)     # banana
print(fruits)   # ['apple', 'cherry', 'date']

# pop(index) - remove at specific index
second = fruits.pop(1)
print(second)   # cherry
print(fruits)   # ['apple', 'date']

# del - delete by index or slice
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print(numbers)  # [2, 3, 4, 5]

del numbers[1:3]
print(numbers)  # [2, 5]

# clear() - remove all items
fruits.clear()
print(fruits)  # []
```

### Part 1.4: List Methods

**Common List Methods:**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# count() - count occurrences
print(numbers.count(1))   # 2
print(numbers.count(5))   # 2

# index() - find first occurrence
print(numbers.index(4))   # 2
print(numbers.index(5))   # 4 (first occurrence)

# reverse() - reverse in place
numbers.reverse()
print(numbers)  # [3, 5, 6, 2, 9, 5, 1, 4, 1, 3]

# sort() - sort in place
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# sort descending
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]

# sorted() - return new sorted list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (unchanged)
print(sorted_list)  # [1, 1, 3, 4, 5]

# copy() - create shallow copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2[0] = 100
print(list1)  # [1, 2, 3] (unchanged)
print(list2)  # [100, 2, 3]
```

### Part 1.5: Iterating Through Lists

**Using for Loop:**
```python
fruits = ["apple", "banana", "cherry"]

# Iterate over items
for fruit in fruits:
    print(fruit)

# Iterate with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# enumerate() - get index and item
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# enumerate with start value
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Iterate in reverse
for fruit in reversed(fruits):
    print(fruit)
```

**Using while Loop:**
```python
numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
```

### Practice Exercise 1: Basic Lists

Create `lists_practice1.py`:
```python
# lists_practice1.py - Basic List Practice

print("=== EXERCISE 1: Shopping List ===")
shopping_list = []

# Add items
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.extend(["butter", "cheese"])

print("Shopping List:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

# Remove an item
shopping_list.remove("bread")
print(f"\nAfter removing bread: {shopping_list}")
print()

print("=== EXERCISE 2: Number Operations ===")
numbers = [45, 23, 67, 12, 89, 34, 56, 78, 90, 11]

print(f"Original list: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Count numbers > 50
count_above_50 = 0
for num in numbers:
    if num > 50:
        count_above_50 += 1
print(f"Numbers > 50: {count_above_50}")
print()

print("=== EXERCISE 3: List Slicing ===")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(f"Full list: {alphabet}")
print(f"First 3: {alphabet[:3]}")
print(f"Last 3: {alphabet[-3:]}")
print(f"Middle (index 3-6): {alphabet[3:7]}")
print(f"Every 2nd element: {alphabet[::2]}")
print(f"Reversed: {alphabet[::-1]}")
print()

print("=== EXERCISE 4: Finding Elements ===")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
search = 50

if search in numbers:
    position = numbers.index(search)
    print(f"Found {search} at index {position}")
else:
    print(f"{search} not found")

# Find all even numbers
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"Even numbers: {evens}")
print()

print("=== EXERCISE 5: List of Lists ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Access specific element
print(f"\nElement at [1][2]: {matrix[1][2]}")  # 6

# Sum all elements
total = 0
for row in matrix:
    for num in row:
        total += num
print(f"Sum of all elements: {total}")
print()

print("=== EXERCISE 6: Student Scores ===")
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 92, 78, 95, 88]

# Display students with scores
print("Student Scores:")
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}")

# Find highest score
highest_score = max(scores)
highest_index = scores.index(highest_score)
print(f"\nHighest score: {students[highest_index]} with {highest_score}")

# Find average
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")

# Students above average
print("\nStudents above average:")
for i in range(len(students)):
    if scores[i] > average:
        print(f"{students[i]}: {scores[i]}")
```

### 📹 Video Resources:

1. **"Python Lists"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=W8KRzm-HUcc
   - Duration: 19 minutes
   - Covers: Creating, accessing, modifying lists

2. **"Python Lists Tutorial"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=9OeznAkyQz4
   - Duration: 15 minutes
   - Covers: List operations and methods

3. **"Python List Methods"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=1yUn-ydsgKk
   - Duration: 12 minutes

### 📚 Text Resources:

1. **Python Official Tutorial - Lists**
   - Link: https://docs.python.org/3/tutorial/introduction.html#lists
   - Official documentation

2. **Real Python - Lists and Tuples**
   - Link: https://realpython.com/python-lists-tuples/
   - Comprehensive guide

3. **W3Schools - Python Lists**
   - Link: https://www.w3schools.com/python/python_lists.asp
   - Interactive examples

### ✅ Checkpoint 1:
- [ ] Can create and access lists
- [ ] Understand indexing and slicing
- [ ] Know list methods (append, remove, etc.)
- [ ] Can iterate through lists
- [ ] Completed basic exercises

---

## 🕑 Session 2: Advanced List Operations (60 minutes)

### Part 2.1: List Comprehensions

**What are List Comprehensions?**
Concise way to create lists based on existing lists.

**Basic Syntax:**
```python
new_list = [expression for item in iterable]
```

**Example 1: Basic Comprehension**
```python
# Without list comprehension
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With list comprehension
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Example 2: Transforming Lists**
```python
# Convert to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

# Get lengths
lengths = [len(fruit) for fruit in fruits]
print(lengths)  # [5, 6, 6]

# Mathematical operations
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

**Example 3: With Conditions**
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Filter long words
words = ["cat", "elephant", "dog", "giraffe", "ant"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['elephant', 'giraffe']

# Numbers divisible by 3
div_by_3 = [n for n in range(20) if n % 3 == 0]
print(div_by_3)  # [0, 3, 6, 9, 12, 15, 18]
```

**Example 4: If-Else in Comprehension**
```python
# Even/odd labels
numbers = [1, 2, 3, 4, 5, 6]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Categorize numbers
numbers = [-5, -2, 0, 3, 7, -1, 4]
categories = ["positive" if n > 0 else "negative" if n < 0 else "zero" for n in numbers]
print(categories)
```

**Example 5: Nested Comprehensions**
```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
```

### Part 2.2: Sorting Lists

**sort() vs sorted():**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - modifies original list
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() - returns new list
original = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(original)
print(original)      # [3, 1, 4, 1, 5, 9, 2, 6] (unchanged)
print(sorted_list)   # [1, 1, 2, 3, 4, 5, 6, 9]
```

**Reverse Sorting:**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Using sorted()
desc = sorted(numbers, reverse=True)
print(desc)
```

**Custom Sorting with key:**
```python
# Sort by length
words = ["python", "java", "c", "javascript", "go", "rust"]
words.sort(key=len)
print(words)  # ['c', 'go', 'java', 'rust', 'python', 'javascript']

# Sort by last letter
words.sort(key=lambda x: x[-1])
print(words)

# Sort by absolute value
numbers = [-5, -2, -8, 3, 1, -1, 4]
numbers.sort(key=abs)
print(numbers)  # [-1, 1, -2, 3, 4, -5, -8]

# Sort list of tuples
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 95)]

# Sort by name
students.sort(key=lambda x: x[0])
print(students)

# Sort by grade (descending)
students.sort(key=lambda x: x[1], reverse=True)
print(students)

# Sort list of dictionaries
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20}
]

people.sort(key=lambda x: x['age'])
for person in people:
    print(f"{person['name']}: {person['age']}")
```

### Part 2.3: Searching in Lists

**Linear Search:**
```python
def linear_search(lst, target):
    """Find index of target in list"""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
print(linear_search(numbers, 30))  # 2
print(linear_search(numbers, 60))  # -1

# Using 'in' operator
print(30 in numbers)     # True
print(60 in numbers)     # False

# Using index() method
try:
    position = numbers.index(30)
    print(f"Found at index {position}")
except ValueError:
    print("Not found")
```

**Binary Search (for sorted lists):**
```python
def binary_search(lst, target):
    """Binary search for sorted list"""
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(numbers, 50))  # 4
print(binary_search(numbers, 35))  # -1
```

**Finding Multiple Occurrences:**
```python
def find_all(lst, target):
    """Find all indices of target"""
    indices = []
    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)
    return indices

numbers = [1, 2, 3, 2, 4, 2, 5]
print(find_all(numbers, 2))  # [1, 3, 5]

# Using list comprehension
indices = [i for i, x in enumerate(numbers) if x == 2]
print(indices)  # [1, 3, 5]
```

### Part 2.4: List Copying

**Shallow Copy:**
```python
# Method 1: copy()
list1 = [1, 2, 3]
list2 = list1.copy()
list2[0] = 100
print(list1)  # [1, 2, 3]
print(list2)  # [100, 2, 3]

# Method 2: list()
list3 = list(list1)

# Method 3: slicing
list4 = list1[:]

# WARNING: Reference (not a copy)
list5 = list1
list5[0] = 999
print(list1)  # [999, 2, 3] - changed!
```

**Deep Copy (for nested lists):**
```python
import copy

# Shallow copy problem with nested lists
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()
list2[0][0] = 999
print(list1)  # [[999, 2], [3, 4]] - inner list changed!

# Deep copy solution
list3 = copy.deepcopy(list1)
list3[0][0] = 111
print(list1)  # [[999, 2], [3, 4]] - unchanged
print(list3)  # [[111, 2], [3, 4]]
```

### Part 2.5: Common List Patterns

**Remove Duplicates:**
```python
# Method 1: Convert to set and back
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)  # Order may change

# Method 2: Preserve order
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  # [1, 2, 3, 4, 5]

# Method 3: Using dict (Python 3.7+)
unique = list(dict.fromkeys(numbers))
print(unique)
```

**Merge Lists:**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Method 1: + operator
merged = list1 + list2
print(merged)  # [1, 2, 3, 4, 5, 6]

# Method 2: extend()
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

# Method 3: unpacking
merged = [*list1, *list2]
```

**Split List:**
```python
def split_list(lst, n):
    """Split list into n parts"""
    chunk_size = len(lst) // n
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(split_list(numbers, 3))  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Practice Exercise 2: Advanced Lists

Create `lists_practice2.py`:
```python
# lists_practice2.py - Advanced List Practice

print("=== EXERCISE 1: List Comprehensions ===")

# Square of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(f"Squares of even numbers: {even_squares}")

# Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Extract vowels
sentence = "Hello World"
vowels = [char for char in sentence if char.lower() in 'aeiou']
print(f"Vowels in '{sentence}': {vowels}")
print()

print("=== EXERCISE 2: Sorting Practice ===")

# Sort by multiple criteria
students = [
    {'name': 'Alice', 'grade': 85, 'age': 20},
    {'name': 'Bob', 'grade': 92, 'age': 19},
    {'name': 'Charlie', 'grade': 85, 'age': 21},
    {'name': 'Diana', 'grade': 92, 'age': 20}
]

# Sort by grade (desc), then by age (asc)
students.sort(key=lambda x: (-x['grade'], x['age']))
print("Students sorted by grade (desc) then age:")
for s in students:
    print(f"{s['name']}: Grade {s['grade']}, Age {s['age']}")
print()

print("=== EXERCISE 3: Data Processing ===")

# Sales data
sales = [120, 150, 180, 90, 200, 110, 170, 160, 140, 190]

print(f"Sales data: {sales}")
print(f"Average: ${sum(sales)/len(sales):.2f}")
print(f"Highest: ${max(sales)}")
print(f"Lowest: ${min(sales)}")

# Days above average
average = sum(sales) / len(sales)
above_avg = [s for s in sales if s > average]
print(f"Days above average: {len(above_avg)}")

# Top 3 days
top_3 = sorted(sales, reverse=True)[:3]
print(f"Top 3 sales days: {top_3}")
print()

print("=== EXERCISE 4: Matrix Operations ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Original:")
for row in matrix:
    print(row)
print("\nTranspose:")
for row in transpose:
    print(row)
print()

print("=== EXERCISE 5: Find Duplicates ===")

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 4]

# Find duplicates
duplicates = []
seen = set()
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)

print(f"Numbers: {numbers}")
print(f"Duplicates: {duplicates}")

# Count frequency
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(f"Frequency: {frequency}")
```

### 📹 Video Resources:

1. **"List Comprehensions"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=3dt4OGnU5sM
   - Duration: 10 minutes

2. **"Python Sorting"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=D3JvDWO-BY4
   - Duration: 11 minutes

### 📚 Text Resources:

1. **Real Python - List Comprehensions**
   - Link: https://realpython.com/list-comprehension-python/

2. **Python Docs - Sorting HOW TO**
   - Link: https://docs.python.org/3/howto/sorting.html

### ✅ Checkpoint 2:
- [ ] Understand list comprehensions
- [ ] Can sort lists effectively
- [ ] Know searching techniques
- [ ] Understand copying vs referencing
- [ ] Completed advanced exercises

---

## 🕒 Session 3: Tuples & Projects (90 minutes)

### Part 3.1: Introduction to Tuples

**What are Tuples?**
Ordered, immutable (unchangeable) collections.

**Creating Tuples:**
```python
# Empty tuple
empty = ()

# Single element (comma required!)
single = (1,)
not_tuple = (1)  # This is just an int!

# Multiple elements
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Without parentheses
coordinates = 10, 20
print(type(coordinates))  # <class 'tuple'>

# Using tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

**Accessing Tuples:**
```python
fruits = ("apple", "banana", "cherry", "date")

# Indexing (same as lists)
print(fruits[0])   # apple
print(fruits[-1])  # date

# Slicing (same as lists)
print(fruits[1:3])  # ('banana', 'cherry')
print(fruits[:2])   # ('apple', 'banana')
print(fruits[::2])  # ('apple', 'cherry')

# Length and membership
print(len(fruits))          # 4
print("banana" in fruits)   # True
```

**Tuple Operations:**
```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# Count and index
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))  # 3
print(numbers.index(4))  # 4
```

**Tuple Unpacking:**
```python
# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"x = {x}, y = {y}")

# Multiple values
person = ("Alice", 25, "New York")
name, age, city = person
print(f"{name} is {age} years old from {city}")

# Swap values
a, b = 10, 20
a, b = b, a  # Swap!
print(f"a = {a}, b = {b}")  # a = 20, b = 10

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}")   # 1
print(f"Middle: {middle}") # [2, 3, 4]
print(f"Last: {last}")     # 5

# Function returns
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}")
```

**Why Use Tuples?**
```python
# 1. Return multiple values from function
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")

# 2. As dictionary keys (lists can't be keys)
locations = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(locations[(1, 2)])  # Point A

# 3. Data integrity (can't be modified)
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# DAYS_OF_WEEK[0] = "Monday"  # Error! Can't modify

# 4. Faster than lists
import sys
list_ex = [1, 2, 3, 4, 5]
tuple_ex = (1, 2, 3, 4, 5)
print(f"List size: {sys.getsizeof(list_ex)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_ex)} bytes")
```

### Part 3.2: Lists vs Tuples

**Comparison:**
```python
# Lists - Mutable
my_list = [1, 2, 3]
my_list[0] = 100  # ✓ Works
my_list.append(4)  # ✓ Works

# Tuples - Immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # ✗ Error!
# my_tuple.append(4)  # ✗ Error!

# When to use Lists:
# - Collection of items might change
# - Need to add/remove/modify elements
# - Order might change

# When to use Tuples:
# - Fixed collection of items
# - Data shouldn't be modified
# - Return multiple values from function
# - Dictionary keys
# - Better performance needed
```

**Converting Between Lists and Tuples:**
```python
# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 4, 5)

# Tuple to list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3, 4, 5]

# Modify tuple (workaround)
original = (1, 2, 3)
temp_list = list(original)
temp_list.append(4)
modified = tuple(temp_list)
print(modified)  # (1, 2, 3, 4)
```

### Project 1: To-Do List Manager

Create `todo_manager.py`:
```python
# todo_manager.py - To-Do List Application

def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("          TO-DO LIST MANAGER")
    print("="*50)
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. View Completed Tasks")
    print("6. View Pending Tasks")
    print("7. Clear All Tasks")
    print("8. Exit")
    print("="*50)

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\n📝 No tasks yet!")
        return
    
    print("\n" + "="*70)
    print(f"{'#':<5} {'Task':<40} {'Status':<15}")
    print("="*70)
    
    for i, task in enumerate(tasks, 1):
        task_text = task['text']
        status = "✓ Complete" if task['completed'] else "⏳ Pending"
        print(f"{i:<5} {task_text:<40} {status:<15}")
    
    print("="*70)
    print(f"Total tasks: {len(tasks)}")
    completed = sum(1 for task in tasks if task['completed'])
    print(f"Completed: {completed}, Pending: {len(tasks) - completed}")

def add_task(tasks):
    """Add a new task"""
    task_text = input("\nEnter task description: ")
    if task_text.strip():
        task = {
            'text': task_text,
            'completed': False
        }
        tasks.append(task)
        print(f"✓ Task '{task_text}' added!")
    else:
        print("❌ Task cannot be empty!")
    return tasks

def complete_task(tasks):
    """Mark a task as complete"""
    if not tasks:
        print("\n❌ No tasks to complete!")
        return tasks
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark complete: "))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1]['completed']:
                print("⚠️  Task is already completed!")
            else:
                tasks[task_num - 1]['completed'] = True
                print(f"✓ Task marked as complete!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")
    
    return tasks

def delete_task(tasks):
    """Delete a task"""
    if not tasks:
        print("\n❌ No tasks to delete!")
        return tasks
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"✓ Task '{deleted['text']}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")
    
    return tasks

def view_completed(tasks):
    """View only completed tasks"""
    completed = [task for task in tasks if task['completed']]
    
    if not completed:
        print("\n✓ No completed tasks!")
        return
    
    print("\n" + "="*50)
    print("COMPLETED TASKS")
    print("="*50)
    for i, task in enumerate(completed, 1):
        print(f"{i}. ✓ {task['text']}")
    print("="*50)

def view_pending(tasks):
    """View only pending tasks"""
    pending = [task for task in tasks if not task['completed']]
    
    if not pending:
        print("\n🎉 All tasks completed!")
        return
    
    print("\n" + "="*50)
    print("PENDING TASKS")
    print("="*50)
    for i, task in enumerate(pending, 1):
        print(f"{i}. ⏳ {task['text']}")
    print("="*50)

def clear_all(tasks):
    """Clear all tasks"""
    if not tasks:
        print("\n📝 No tasks to clear!")
        return tasks
    
    confirm = input(f"\n⚠️  Delete all {len(tasks)} tasks? (yes/no): ")
    if confirm.lower() == 'yes':
        tasks.clear()
        print("✓ All tasks cleared!")
    else:
        print("Cancelled.")
    return tasks

def main():
    """Main program loop"""
    tasks = []
    
    print("\n👋 Welcome to To-Do List Manager!")
    
    while True:
        display_menu()
        choice = input("\nSelect option (1-8): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            tasks = add_task(tasks)
        elif choice == '3':
            tasks = complete_task(tasks)
        elif choice == '4':
            tasks = delete_task(tasks)
        elif choice == '5':
            view_completed(tasks)
        elif choice == '6':
            view_pending(tasks)
        elif choice == '7':
            tasks = clear_all(tasks)
        elif choice == '8':
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("\n❌ Invalid option! Please select 1-8")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Project 2: Inventory Management System

Create `inventory_system.py`:
```python
# inventory_system.py - Store Inventory Manager

def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Remove Product")
    print("6. Low Stock Alert")
    print("7. Total Inventory Value")
    print("8. Exit")
    print("="*60)

def add_product(inventory):
    """Add a new product"""
    print("\n--- Add New Product ---")
    
    product_id = input("Product ID: ")
    
    # Check if ID already exists
    for product in inventory:
        if product['id'] == product_id:
            print("❌ Product ID already exists!")
            return inventory
    
    name = input("Product Name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit: $"))
    
    product = {
        'id': product_id,
        'name': name,
        'category': category,
        'quantity': quantity,
        'price': price
    }
    
    inventory.append(product)
    print(f"✓ Product '{name}' added successfully!")
    return inventory

def view_all_products(inventory):
    """Display all products"""
    if not inventory:
        print("\n📦 No products in inventory!")
        return
    
    print("\n" + "="*90)
    print(f"{'ID':<10} {'Name':<20} {'Category':<15} {'Quantity':<10} {'Price':<10} {'Value':<10}")
    print("="*90)
    
    for product in inventory:
        value = product['quantity'] * product['price']
        print(f"{product['id']:<10} "
              f"{product['name']:<20} "
              f"{product['category']:<15} "
              f"{product['quantity']:<10} "
              f"${product['price']:<9.2f} "
              f"${value:<9.2f}")
    
    print("="*90)
    print(f"Total products: {len(inventory)}")

def search_product(inventory):
    """Search for a product"""
    if not inventory:
        print("\n📦 No products to search!")
        return
    
    search_term = input("\nEnter product name or ID: ").lower()
    found = []
    
    for product in inventory:
        if (search_term in product['name'].lower() or 
            search_term in product['id'].lower()):
            found.append(product)
    
    if found:
        print(f"\n✓ Found {len(found)} product(s):")
        print("="*80)
        for product in found:
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Category: {product['category']}")
            print(f"Quantity: {product['quantity']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Total Value: ${product['quantity'] * product['price']:.2f}")
            print("-"*80)
    else:
        print(f"\n❌ No products found matching '{search_term}'")

def update_stock(inventory):
    """Update product stock"""
    if not inventory:
        print("\n📦 No products to update!")
        return inventory
    
    product_id = input("\nEnter product ID: ")
    
    for product in inventory:
        if product['id'] == product_id:
            print(f"\nCurrent stock of '{product['name']}': {product['quantity']}")
            print("1. Add stock")
            print("2. Remove stock")
            print("3. Set stock")
            
            choice = input("Select option: ")
            
            try:
                if choice == '1':
                    amount = int(input("Quantity to add: "))
                    product['quantity'] += amount
                    print(f"✓ Added {amount} units. New stock: {product['quantity']}")
                elif choice == '2':
                    amount = int(input("Quantity to remove: "))
                    if amount > product['quantity']:
                        print("❌ Not enough stock!")
                    else:
                        product['quantity'] -= amount
                        print(f"✓ Removed {amount} units. New stock: {product['quantity']}")
                elif choice == '3':
                    amount = int(input("New quantity: "))
                    product['quantity'] = amount
                    print(f"✓ Stock set to {amount}")
                else:
                    print("❌ Invalid option!")
            except ValueError:
                print("❌ Please enter a valid number!")
            
            return inventory
    
    print(f"❌ Product ID '{product_id}' not found!")
    return inventory

def remove_product(inventory):
    """Remove a product"""
    if not inventory:
        print("\n📦 No products to remove!")
        return inventory
    
    product_id = input("\nEnter product ID to remove: ")
    
    for i, product in enumerate(inventory):
        if product['id'] == product_id:
            confirm = input(f"Remove '{product['name']}'? (yes/no): ")
            if confirm.lower() == 'yes':
                inventory.pop(i)
                print(f"✓ Product removed!")
            else:
                print("Cancelled.")
            return inventory
    
    print(f"❌ Product ID '{product_id}' not found!")
    return inventory

def low_stock_alert(inventory, threshold=10):
    """Show products with low stock"""
    if not inventory:
        print("\n📦 No products in inventory!")
        return
    
    low_stock = [p for p in inventory if p['quantity'] < threshold]
    
    if not low_stock:
        print(f"\n✓ All products have adequate stock (>= {threshold})")
        return
    
    print(f"\n⚠️  LOW STOCK ALERT (< {threshold} units)")
    print("="*70)
    print(f"{'ID':<10} {'Name':<25} {'Quantity':<10} {'Category':<20}")
    print("="*70)
    
    for product in low_stock:
        print(f"{product['id']:<10} "
              f"{product['name']:<25} "
              f"{product['quantity']:<10} "
              f"{product['category']:<20}")
    
    print("="*70)
    print(f"Total low stock items: {len(low_stock)}")

def total_inventory_value(inventory):
    """Calculate total inventory value"""
    if not inventory:
        print("\n📦 No products in inventory!")
        return
    
    total_value = sum(p['quantity'] * p['price'] for p in inventory)
    total_items = sum(p['quantity'] for p in inventory)
    
    # Value by category
    category_values = {}
    for product in inventory:
        cat = product['category']
        value = product['quantity'] * product['price']
        category_values[cat] = category_values.get(cat, 0) + value
    
    print("\n" + "="*50)
    print("INVENTORY VALUE REPORT")
    print("="*50)
    print(f"Total Items: {total_items}")
    print(f"Total Products: {len(inventory)}")
    print(f"Total Value: ${total_value:,.2f}")
    print("\nValue by Category:")
    for cat, value in sorted(category_values.items()):
        print(f"  {cat}: ${value:,.2f}")
    print("="*50)

def main():
    """Main program loop"""
    inventory = []
    
    # Sample data
    inventory.append({'id': 'P001', 'name': 'Laptop', 'category': 'Electronics', 'quantity': 15, 'price': 899.99})
    inventory.append({'id': 'P002', 'name': 'Mouse', 'category': 'Electronics', 'quantity': 50, 'price': 19.99})
    inventory.append({'id': 'P003', 'name': 'Notebook', 'category': 'Stationery', 'quantity': 5, 'price': 3.99})
    
    print("\n📦 Welcome to Inventory Management System!")
    
    while True:
        display_menu()
        choice = input("\nSelect option (1-8): ")
        
        if choice == '1':
            inventory = add_product(inventory)
        elif choice == '2':
            view_all_products(inventory)
        elif choice == '3':
            search_product(inventory)
        elif choice == '4':
            inventory = update_stock(inventory)
        elif choice == '5':
            inventory = remove_product(inventory)
        elif choice == '6':
            low_stock_alert(inventory)
        elif choice == '7':
            total_inventory_value(inventory)
        elif choice == '8':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid option!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Project 3: Data Analysis Tool

Create `data_analyzer.py`:
```python
# data_analyzer.py - Simple Data Analysis Tool

def calculate_statistics(data):
    """Calculate basic statistics"""
    if not data:
        return None
    
    sorted_data = sorted(data)
    n = len(data)
    
    stats = {
        'count': n,
        'sum': sum(data),
        'mean': sum(data) / n,
        'median': sorted_data[n//2] if n % 2 != 0 else (sorted_data[n//2-1] + sorted_data[n//2]) / 2,
        'min': min(data),
        'max': max(data),
        'range': max(data) - min(data)
    }
    
    # Variance and standard deviation
    mean = stats['mean']
    variance = sum((x - mean) ** 2 for x in data) / n
    stats['variance'] = variance
    stats['std_dev'] = variance ** 0.5
    
    return stats

def display_statistics(stats):
    """Display statistics in formatted table"""
    print("\n" + "="*50)
    print("STATISTICAL SUMMARY")
    print("="*50)
    print(f"Count:               {stats['count']}")
    print(f"Sum:                 {stats['sum']:.2f}")
    print(f"Mean (Average):      {stats['mean']:.2f}")
    print(f"Median:              {stats['median']:.2f}")
    print(f"Minimum:             {stats['min']:.2f}")
    print(f"Maximum:             {stats['max']:.2f}")
    print(f"Range:               {stats['range']:.2f}")
    print(f"Variance:            {stats['variance']:.2f}")
    print(f"Standard Deviation:  {stats['std_dev']:.2f}")
    print("="*50)

def find_outliers(data, threshold=2):
    """Find outliers using standard deviation method"""
    if not data:
        return []
    
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    
    outliers = [x for x in data if abs(x - mean) > threshold * std_dev]
    return outliers

def create_frequency_distribution(data, bins=5):
    """Create frequency distribution"""
    if not data:
        return []
    
    min_val = min(data)
    max_val = max(data)
    bin_width = (max_val - min_val) / bins
    
    distribution = []
    for i in range(bins):
        bin_start = min_val + i * bin_width
        bin_end = bin_start + bin_width
        count = sum(1 for x in data if bin_start <= x < bin_end or (i == bins-1 and x == bin_end))
        distribution.append((f"{bin_start:.1f}-{bin_end:.1f}", count))
    
    return distribution

def display_histogram(distribution):
    """Display simple text histogram"""
    if not distribution:
        return
    
    max_count = max(count for _, count in distribution)
    scale = 50 / max_count if max_count > 0 else 1
    
    print("\n" + "="*70)
    print("FREQUENCY DISTRIBUTION")
    print("="*70)
    
    for range_label, count in distribution:
        bar = "█" * int(count * scale)
        print(f"{range_label:>15} | {bar} {count}")
    
    print("="*70)

def compare_datasets(data1, data2, label1="Dataset 1", label2="Dataset 2"):
    """Compare two datasets"""
    stats1 = calculate_statistics(data1)
    stats2 = calculate_statistics(data2)
    
    print("\n" + "="*70)
    print("DATASET COMPARISON")
    print("="*70)
    print(f"{'Statistic':<20} {label1:>20} {label2:>20}")
    print("-"*70)
    print(f"{'Count':<20} {stats1['count']:>20} {stats2['count']:>20}")
    print(f"{'Mean':<20} {stats1['mean']:>20.2f} {stats2['mean']:>20.2f}")
    print(f"{'Median':<20} {stats1['median']:>20.2f} {stats2['median']:>20.2f}")
    print(f"{'Min':<20} {stats1['min']:>20.2f} {stats2['min']:>20.2f}")
    print(f"{'Max':<20} {stats1['max']:>20.2f} {stats2['max']:>20.2f}")
    print(f"{'Std Dev':<20} {stats1['std_dev']:>20.2f} {stats2['std_dev']:>20.2f}")
    print("="*70)

def main():
    """Main program"""
    print("="*60)
    print("         DATA ANALYSIS TOOL")
    print("="*60)
    
    # Sample data
    sales_data = [120, 150, 180, 90, 200, 110, 170, 160, 140, 190, 
                  210, 95, 175, 185, 145, 155, 165, 125, 135, 195]
    
    temperatures = [72, 75, 68, 70, 73, 76, 71, 69, 74, 77,
                   78, 70, 72, 75, 73, 71, 76, 74, 69, 72]
    
    while True:
        print("\n" + "="*60)
        print("MENU")
        print("="*60)
        print("1. Analyze Sales Data")
        print("2. Analyze Temperature Data")
        print("3. Compare Datasets")
        print("4. Find Outliers (Sales)")
        print("5. Show Histogram (Sales)")
        print("6. Enter Custom Data")
        print("7. Exit")
        print("="*60)
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            print("\n--- SALES DATA ANALYSIS ---")
            print(f"Data: {sales_data}")
            stats = calculate_statistics(sales_data)
            display_statistics(stats)
        
        elif choice == '2':
            print("\n--- TEMPERATURE DATA ANALYSIS ---")
            print(f"Data: {temperatures}")
            stats = calculate_statistics(temperatures)
            display_statistics(stats)
        
        elif choice == '3':
            compare_datasets(sales_data, temperatures, "Sales ($)", "Temperature (°F)")
        
        elif choice == '4':
            outliers = find_outliers(sales_data)
            if outliers:
                print(f"\n⚠️  Outliers found: {outliers}")
            else:
                print("\n✓ No outliers detected")
        
        elif choice == '5':
            distribution = create_frequency_distribution(sales_data, bins=5)
            display_histogram(distribution)
        
        elif choice == '6':
            print("\n--- Enter Custom Data ---")
            data_str = input("Enter numbers separated by spaces: ")
            try:
                custom_data = [float(x) for x in data_str.split()]
                if custom_data:
                    stats = calculate_statistics(custom_data)
                    display_statistics(stats)
                else:
                    print("❌ No data entered!")
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
        
        elif choice == '7':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("\n❌ Invalid option!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### 📹 Video Resources:

1. **"Python Tuples"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=NI26dqhs2Rk
   - Duration: 8 minutes

2. **"Lists vs Tuples"** by Real Python
   - Link: https://realpython.com/python-lists-tuples/
   - Comprehensive comparison

### ✅ Checkpoint 3:
- [ ] Understand tuples
- [ ] Know list vs tuple differences
- [ ] Can use tuple unpacking
- [ ] Built all 3 projects
- [ ] Projects working correctly

---

## 📝 Day 6 Summary & Achievements

### What You Mastered Today:

✅ **Lists:**
- Creating and accessing lists
- List methods (append, remove, sort, etc.)
- List comprehensions
- Sorting and searching
- List copying

✅ **Tuples:**
- Creating immutable sequences
- Tuple operations
- Tuple unpacking
- When to use tuples vs lists

✅ **Projects:**
- To-Do list manager
- Inventory system
- Data analyzer

---

## 🎯 Assignments

### Mandatory:
- [ ] All practice exercises
- [ ] Build all 3 projects
- [ ] Understand comprehensions
- [ ] Push to GitHub

### Challenges:

**1. Gradebook System**
- Store student grades in lists
- Calculate class statistics
- Sort by performance
- Generate reports

**2. Shopping Cart**
- Add/remove items
- Calculate totals with tax
- Apply discounts
- Generate receipt

**3. Data Processor**
- Read numerical data
- Find patterns
- Statistical analysis
- Visualization (text-based)

---

## 📊 Self-Assessment

1. What's the output?
```python
nums = [1, 2, 3]
nums.append([4, 5])
print(len(nums))
```
<details>
<summary>Answer</summary>
4 (list is added as single element)
</details>

2. What does this comprehension create?
```python
[x**2 for x in range(5) if x % 2 == 0]
```
<details>
<summary>Answer</summary>
[0, 4, 16] (squares of even numbers 0-4)
</details>

3. Can you modify a tuple?
<details>
<summary>Answer</summary>
No, tuples are immutable
</details>

4. What's the difference between sort() and sorted()?
<details>
<summary>Answer</summary>
sort() modifies in place, sorted() returns new list
</details>

---

## 🚀 Git Commit

```bash
git add .
git commit -m "Day 6: Lists, tuples, and 3 data projects"
git push
```

---

## ✅ Completion Checklist

### Concepts:
- [ ] List creation/access
- [ ] List methods
- [ ] Slicing
- [ ] List comprehensions
- [ ] Sorting/searching
- [ ] Tuples
- [ ] Tuple unpacking

### Projects:
- [ ] To-Do manager
- [ ] Inventory system
- [ ] Data analyzer

**Overall: ____%**

---

## 📅 Tomorrow: Day 7

- **Dictionaries**
- **Sets**
- **Dictionary methods**
- **Set operations**

---

**Day 6 of 168 Complete!** 🎉

*"Lists are the workhorses of Python data structures."*