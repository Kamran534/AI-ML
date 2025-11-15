# Day 1: Python Installation, Environment Setup & Basic Syntax

**Duration:** 3-4 hours | **Date:** 11/13/2025 | **Status:** ⬜ Not Started | ⬜ In Progress | ✅ Completed

---

## 🎯 Today's Goals

By the end of today, you will:
- ✅ Install Python 3.10+ on your computer
- ✅ Set up VS Code with Python extensions
- ✅ Install and configure Git
- ✅ Create your first GitHub repository
- ✅ Write and run your first Python program
- ✅ Understand Python basic syntax and variables

---

## 📋 Pre-Session Checklist

Before starting, ensure you have:
- [ ] A computer (Windows/Mac/Linux)
- [ ] Stable internet connection
- [ ] At least 5GB free disk space
- [ ] Admin/sudo access (for installations)
- [ ] A notepad for taking notes
- [ ] 3-4 hours of focused time

---

## 🕐 Session 1: Python Installation (45 minutes)

### Step 1.1: Download Python

**For Windows Users:**

1. Visit the official Python website: https://www.python.org/downloads/
2. Click the yellow "Download Python 3.12.x" button (or latest version)
3. The download will start automatically (python-3.12.x-amd64.exe)

**Important Settings During Installation:**
- ✅ **CHECK** "Add Python to PATH" (CRITICAL!)
- ✅ **CHECK** "Install pip"
- Click "Install Now"
- Wait for installation to complete

**For Mac Users:**

**Option 1: Official Installer**
1. Visit: https://www.python.org/downloads/macos/
2. Download the macOS installer (.pkg file)
3. Double-click and follow the installer

**Option 2: Using Homebrew (Recommended)**
```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.12
```

**For Linux Users (Ubuntu/Debian):**

```bash
# Update package list
sudo apt update

# Install Python 3.12
sudo apt install python3.12 python3.12-venv python3-pip

# Verify installation
python3 --version
```

### Step 1.2: Verify Python Installation

Open Terminal/Command Prompt and type:

```bash
# Check Python version
python --version
# OR on Mac/Linux
python3 --version

# Expected output: Python 3.12.x or Python 3.10+

# Check pip installation
pip --version
# OR
pip3 --version

# Expected output: pip 23.x.x from ...
```

**Troubleshooting:**

If `python --version` doesn't work:
- **Windows:** Restart your computer or manually add Python to PATH
- **Mac/Linux:** Use `python3` instead of `python`
- Check: https://realpython.com/installing-python/

### 📹 Video Resources for Installation:

1. **"Python Installation Tutorial for Beginners"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=YYXdXT2l-Gg
   - Duration: 6 minutes
   - Covers: Windows, Mac installation step-by-step

2. **"How to Install Python on Windows 10/11"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=YYXdXT2l-Gg
   - Duration: 7 minutes
   - Covers: PATH setup, verification

3. **Official Python Documentation - Installation**
   - Link: https://docs.python.org/3/using/index.html
   - Text guide for all operating systems

### ✅ Checkpoint 1:
```bash
# Run this command successfully
python --version
# Output should be: Python 3.10 or higher
```

---

## 🕑 Session 2: VS Code Installation & Setup (45 minutes)

### Step 2.1: Download and Install VS Code

1. Visit: https://code.visualstudio.com/
2. Click "Download for [Your OS]"
3. Run the installer
4. Follow default installation options

**Windows:** Run .exe installer
**Mac:** Drag VS Code to Applications folder
**Linux:** 
```bash
sudo snap install code --classic
# OR download .deb/.rpm from website
```

### Step 2.2: Install Essential VS Code Extensions

Open VS Code, then:

**Method 1: Using Extensions Sidebar**
1. Click Extensions icon (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
2. Search and install these extensions:

**Required Extensions:**

1. **Python** (by Microsoft)
   - Extension ID: ms-python.python
   - Features: IntelliSense, debugging, Jupyter support
   - Install: Search "Python" → Click Install

2. **Pylance** (by Microsoft)
   - Extension ID: ms-python.vscode-pylance
   - Features: Fast language server, type checking
   - Usually installs with Python extension

3. **Python Indent** (by Kevin Rose)
   - Extension ID: KevinRose.vsc-python-indent
   - Features: Correct Python indentation

**Optional but Recommended:**

4. **GitLens** (by GitKraken)
   - Extension ID: eamodio.gitlens
   - Features: Git visualization and history

5. **Code Runner** (by Jun Han)
   - Extension ID: formulahendry.code-runner
   - Features: Run code with right-click

6. **Jupyter** (by Microsoft)
   - Extension ID: ms-toolsai.jupyter
   - Features: Jupyter notebook support

7. **Material Icon Theme** (by Philipp Kief)
   - Extension ID: PKief.material-icon-theme
   - Features: Better file icons (optional)

### Step 2.3: Configure Python in VS Code

1. Open VS Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Python: Select Interpreter"
4. Choose the Python version you installed (e.g., Python 3.12.x)

**Create Your First Python File:**

1. File → New File (or `Ctrl+N`)
2. Save as `hello.py` (File → Save As)
3. VS Code will recognize it as Python and activate extensions

### 📹 Video Resources for VS Code:

1. **"Visual Studio Code for Python Developers"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=-nh9rCzPJ20
   - Duration: 13 minutes
   - Covers: Installation, extensions, configuration

2. **"VS Code Python Tutorial"** by Tech With Tim
   - Link: https://www.youtube.com/watch?v=W--_EOzdTHk
   - Duration: 10 minutes
   - Covers: Setup, running Python code

3. **Official VS Code Python Tutorial**
   - Link: https://code.visualstudio.com/docs/python/python-tutorial
   - Text guide with screenshots

### ✅ Checkpoint 2:
- [ ] VS Code installed and running
- [ ] Python extension installed (green checkmark)
- [ ] Python interpreter selected
- [ ] Can create and save .py files

---

## 🕒 Session 3: Git Installation & GitHub Setup (30 minutes)

### Step 3.1: Install Git

**For Windows:**

1. Download from: https://git-scm.com/download/win
2. Run the installer (Git-2.x.x-64-bit.exe)
3. **Important Installation Options:**
   - Use Visual Studio Code as Git's default editor
   - Let Git decide the default branch name
   - Git from the command line and also from 3rd-party software
   - Use the OpenSSL library
   - Checkout Windows-style, commit Unix-style line endings
   - Use MinTTY (default)
   - Default (fast-forward or merge)
   - Git Credential Manager
   - Enable file system caching

**For Mac:**

**Option 1: Install via Homebrew**
```bash
brew install git
```

**Option 2: Install via Xcode Command Line Tools**
```bash
xcode-select --install
```

**For Linux:**
```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git

# Arch Linux
sudo pacman -S git
```

### Step 3.2: Verify Git Installation

```bash
git --version
# Expected output: git version 2.x.x
```

### Step 3.3: Configure Git

Open Terminal/Command Prompt and run:

```bash
# Set your name (will appear in commits)
git config --global user.name "Your Name"

# Set your email (should match GitHub email)
git config --global user.email "your.email@example.com"

# Set default branch name to 'main'
git config --global init.defaultBranch main

# Verify configuration
git config --list
```

### Step 3.4: Create GitHub Account

1. Visit: https://github.com/
2. Click "Sign up"
3. Enter email, create password, choose username
4. Verify email address
5. Complete the setup wizard

**Choose a Professional Username:**
- Use your real name or professional alias
- Keep it simple and memorable
- Examples: johnsmith, john-smith-dev, jsmith-ml

### Step 3.5: Generate SSH Key (Optional but Recommended)

**Why:** Allows secure connection to GitHub without entering password

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter for default location
# Press Enter twice for no passphrase (or create one for security)

# Copy SSH key to clipboard

# On Windows (Git Bash):
clip < ~/.ssh/id_ed25519.pub

# On Mac:
pbcopy < ~/.ssh/id_ed25519.pub

# On Linux:
cat ~/.ssh/id_ed25519.pub
# Then manually copy the output
```

**Add SSH Key to GitHub:**

1. Go to GitHub.com → Click your profile → Settings
2. Click "SSH and GPG keys" in left sidebar
3. Click "New SSH key"
4. Title: "My Computer" (or descriptive name)
5. Paste the SSH key
6. Click "Add SSH key"

**Test SSH Connection:**
```bash
ssh -T git@github.com
# Expected: "Hi username! You've successfully authenticated..."
```

### 📹 Video Resources for Git:

1. **"Git and GitHub for Beginners"** by freeCodeCamp
   - Link: https://www.youtube.com/watch?v=RGOj5yH7evk
   - Duration: 1 hour (watch first 15 minutes today)
   - Covers: Installation, basic concepts, GitHub setup

2. **"Git Tutorial for Beginners"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=8JJ101D3knE
   - Duration: 1 hour (watch first 20 minutes)
   - Covers: Installation, configuration, basic commands

3. **"How to Use Git and GitHub"** by Corey Schafer
   - Link: https://www.youtube.com/watch?v=HVsySz-h9r4
   - Duration: 20 minutes
   - Covers: Setup, first repository, commits

4. **Official GitHub Guides**
   - Link: https://docs.github.com/en/get-started/quickstart
   - Text tutorials for getting started

### ✅ Checkpoint 3:
- [ ] Git installed and verified
- [ ] Git configured with name and email
- [ ] GitHub account created
- [ ] SSH key added (optional)

---

## 🕓 Session 4: Your First Python Program (60 minutes)

### Step 4.1: Python Interactive Mode (REPL)

REPL = Read-Eval-Print Loop (Interactive Python shell)

**Launch Python REPL:**
```bash
# In Terminal/Command Prompt
python
# OR
python3
```

You'll see:
```
Python 3.12.0 (main, Nov  5 2024)
>>> 
```

**Try These Commands:**

```python
# Simple arithmetic
>>> 2 + 2
4

>>> 10 * 5
50

>>> 15 / 3
5.0

>>> 2 ** 8  # 2 to the power of 8
256

# Print messages
>>> print("Hello, World!")
Hello, World!

>>> print("My name is", "Python")
My name is Python

# Variables
>>> name = "Alice"
>>> age = 25
>>> print(name, "is", age, "years old")
Alice is 25 years old

# To exit REPL
>>> exit()
# OR press Ctrl+D (Mac/Linux) or Ctrl+Z then Enter (Windows)
```

### Step 4.2: Create Your First Python Script

**Open VS Code and create `hello.py`:**

```python
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
```

**Run the Program:**

**Method 1: Using Terminal in VS Code**
```bash
python hello.py
```

**Method 2: Using VS Code Run Button**
- Click the ▶ (Play) button in top-right corner
- OR Right-click in editor → "Run Python File in Terminal"
- OR Press `Ctrl+Alt+N` (if Code Runner installed)

**Expected Output:**
```
Hello, World!
Welcome to Python Programming!
10 + 5 = 15
My name is: Your Name Here
I am learning Python!
```

### Step 4.3: Python Basic Syntax

**Comments:**
```python
# This is a single-line comment
# Python ignores anything after #

"""
This is a multi-line comment
Also called a docstring
Can span multiple lines
"""

'''
You can also use single quotes
for multi-line comments
'''
```

**Print Function:**
```python
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
```

**Variables:**
```python
# Variable assignment
x = 5
name = "Alice"
price = 19.99
is_student = True

# Multiple assignment
a, b, c = 1, 2, 3

# Same value to multiple variables
x = y = z = 0

# Variable naming rules:
# ✅ Valid names
my_variable = 1
myVariable = 2  # camelCase
my_variable_2 = 3
_private = 4
MY_CONSTANT = 5

# ❌ Invalid names
# 2my_variable = 1  # Can't start with number
# my-variable = 2   # No hyphens
# my variable = 3   # No spaces
# class = 4         # Can't use keywords
```

**Data Types:**
```python
# Integer (whole numbers)
age = 25
year = 2024
negative = -10

# Float (decimal numbers)
price = 19.99
pi = 3.14159
temperature = -5.5

# String (text)
name = "Alice"
message = 'Hello, World!'
multi_line = """This is a
multi-line
string"""

# Boolean (True/False)
is_student = True
is_working = False

# Check data type
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
```

### Step 4.4: Practice Exercises

**Exercise 1: Personal Information**

Create a file `about_me.py`:

```python
# about_me.py - Personal Information Program

# Store your information
first_name = "John"
last_name = "Doe"
age = 25
city = "New York"
country = "USA"
is_student = True

# Display information
print("=== My Information ===")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Location: {city}, {country}")
print(f"Student Status: {is_student}")

# Calculate future age
years_ahead = 10
future_age = age + years_ahead
print(f"\nIn {years_ahead} years, I will be {future_age} years old")
```

**Exercise 2: Simple Calculator**

Create `calculator.py`:

```python
# calculator.py - Basic Arithmetic

# Numbers to work with
num1 = 10
num2 = 3

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
integer_division = num1 // num2
remainder = num1 % num2
power = num1 ** num2

# Display results
print("=== Calculator Results ===")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {integer_division}")
print(f"{num1} % {num2} = {remainder}")
print(f"{num1} ** {num2} = {power}")
```

**Exercise 3: Message Formatter**

Create `messages.py`:

```python
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
```

### 📹 Video Resources for Python Basics:

1. **"Python for Beginners - Learn Python in 1 Hour"** by Programming with Mosh
   - Link: https://www.youtube.com/watch?v=kqtD5dpn9C8
   - Duration: 1 hour
   - Covers: Variables, data types, print, input

2. **"Python Tutorial for Beginners"** by Corey Schafer
   - Link: https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
   - Watch videos 1-3
   - Covers: Setup, variables, data types

3. **"Python Crash Course for Beginners"** by freeCodeCamp
   - Link: https://www.youtube.com/watch?v=rfscVS0vtbw
   - Watch first 30 minutes
   - Comprehensive beginner guide

### 📚 Text Resources:

1. **Official Python Tutorial - Introduction**
   - Link: https://docs.python.org/3/tutorial/introduction.html
   - Covers: Numbers, strings, first steps

2. **Real Python - Python Basics**
   - Link: https://realpython.com/python-basics/
   - Interactive tutorial for beginners

3. **W3Schools Python Tutorial**
   - Link: https://www.w3schools.com/python/
   - Great for quick reference and examples

4. **Automate the Boring Stuff with Python - Chapter 1**
   - Link: https://automatetheboringstuff.com/2e/chapter1/
   - Free online book, beginner-friendly

### ✅ Checkpoint 4:
- [ ] Created and ran hello.py successfully
- [ ] Understand print() function
- [ ] Can create and use variables
- [ ] Know basic data types
- [ ] Completed at least 2 practice exercises

---

## 🕔 Session 5: Create Your First GitHub Repository (30 minutes)

### Step 5.1: Initialize Local Git Repository

**In VS Code Terminal:**

```bash
# Navigate to your project folder (or create new one)
mkdir python-learning
cd python-learning

# Initialize Git repository
git init

# Check status
git status
```

### Step 5.2: Create README File

Create `README.md` in your folder:

```markdown
# Python Learning Journey

## About This Repository
This repository contains my Python learning projects and exercises as I work through my AI career roadmap.

## Day 1 Achievements
- ✅ Installed Python 3.12
- ✅ Set up VS Code with Python extensions
- ✅ Installed and configured Git
- ✅ Created first Python program
- ✅ Learned Python basics: variables, data types, print

## Files in This Repository
- `hello.py` - My first Python program
- `about_me.py` - Personal information script
- `calculator.py` - Basic arithmetic operations
- `messages.py` - String formatting practice

## Next Steps
- Learn control flow (if/else, loops)
- Practice with more exercises
- Build small projects

## Contact
- GitHub: [@yourusername](https://github.com/yourusername)
- Learning Start Date: [Today's Date]

---
*Day 1 of my 6-month AI career roadmap*
```

### Step 5.3: Add and Commit Files

```bash
# Add all files to staging
git add .

# OR add specific files
git add hello.py
git add README.md

# Check what's staged
git status

# Commit with message
git commit -m "Day 1: First Python programs and setup"

# View commit history
git log
```

### Step 5.4: Create GitHub Repository

1. Go to GitHub.com
2. Click the "+" icon (top-right) → "New repository"
3. Repository name: `python-learning` (or your choice)
4. Description: "My Python learning journey - 6 month AI roadmap"
5. Choose: **Public** (so others can see your progress)
6. **DO NOT** check "Initialize with README" (we already have one)
7. Click "Create repository"

### Step 5.5: Push to GitHub

GitHub will show you commands. Use these:

```bash
# Connect local repository to GitHub (HTTPS method)
git remote add origin https://github.com/YOUR_USERNAME/python-learning.git

# OR if using SSH (recommended if you set up SSH key)
git remote add origin git@github.com:YOUR_USERNAME/python-learning.git

# Verify remote
git remote -v

# Push your code to GitHub
git branch -M main
git push -u origin main

# Enter your GitHub username and password (or it will use SSH)
```

**Success!** Your code is now on GitHub! Visit:
`https://github.com/YOUR_USERNAME/python-learning`

### Step 5.6: Basic Git Commands Reference

```bash
# Check status of files
git status

# Add files to staging
git add filename.py        # Add specific file
git add .                  # Add all files

# Commit changes
git commit -m "Commit message describing changes"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log

# View commit history (one line per commit)
git log --oneline

# Undo changes (before commit)
git restore filename.py

# Create new branch
git branch branch-name

# Switch branch
git checkout branch-name

# Merge branch
git merge branch-name
```

### ✅ Checkpoint 5:
- [ ] Git repository initialized
- [ ] README.md created
- [ ] Files committed locally
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Can view repository online

---

## 📝 Day 1 Summary & Reflection

### What You Accomplished Today:

✅ **Environment Setup:**
- Installed Python 3.10+
- Configured VS Code with extensions
- Installed Git and created GitHub account

✅ **Programming Basics:**
- Wrote first Python program
- Learned variables and data types
- Used print() function
- Created 3+ practice programs

✅ **Version Control:**
- Initialized Git repository
- Created README documentation
- Pushed code to GitHub

### Key Concepts Learned:

1. **Python Basics:**
   - Variables (x = 5)
   - Data types (int, float, str, bool)
   - Print function
   - Comments
   - Basic arithmetic

2. **Development Tools:**
   - VS Code interface
   - Terminal/Command Prompt
   - Python REPL
   - Git commands

3. **Best Practices:**
   - Code comments
   - Meaningful variable names
   - Version control
   - Documentation (README)

---

## 🎯 Today's Assignments

### Mandatory:
- [ ] Complete all installation steps
- [ ] Run hello.py successfully
- [ ] Create at least 2 practice programs
- [ ] Push code to GitHub

### Optional Challenges:
- [ ] Create a program that calculates BMI
- [ ] Make a program that displays a formatted receipt
- [ ] Write a program that creates ASCII art with your name
- [ ] Explore Python built-in functions: len(), type(), str(), int()

### Example Challenge: BMI Calculator

Create `bmi_calculator.py`:
```python
# bmi_calculator.py - Body Mass Index Calculator

# Get user input
name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print(f"\n=== BMI Results for {name} ===")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")

# BMI Categories (we'll add if/else logic on Day 3)
print("\nBMI Categories:")
print("Underweight: < 18.5")
print("Normal: 18.5 - 24.9")
print("Overweight: 25 - 29.9")
print("Obese: >= 30")
```

---

## 📖 Additional Learning Resources

### Interactive Learning Platforms:

1. **Python.org Official Tutorial**
   - Link: https://docs.python.org/3/tutorial/
   - Start with sections 1-3

2. **Python Tutor (Code Visualizer)**
   - Link: https://pythontutor.com/
   - Visualize how your code executes line by line

3. **Programiz Python Tutorial**
   - Link: https://www.programiz.com/python-programming
   - Beginner-friendly with examples

4. **Codecademy - Learn Python 3**
   - Link: https://www.codecademy.com/learn/learn-python-3
   - Interactive exercises (free tier available)

### YouTube Playlists:

1. **Python Tutorial for Beginners** by Corey Schafer
   - Link: https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
   - Watch videos 1-5

2. **Python for Everybody** by Dr. Chuck
   - Link: https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p
   - Comprehensive university course

### Books (Free Online):

1. **"Automate the Boring Stuff with Python"** by Al Sweigart
   - Link: https://automatetheboringstuff.com/
   - Chapters 0-1 for today

2. **"Think Python"** by Allen Downey
   - Link: https://greenteapress.com/wp/think-python-2e/
   - Chapters 1-2

3. **"Python for Beginners"** - Microsoft
   - Link: https://docs.microsoft.com/en-us/learn/paths/beginner-python/

### Practice Websites:

1. **HackerRank - Python Track**
   - Link: https://www.hackerrank.com/domains/python
   - Start with "Introduction" section

2. **Codewars - Python Challenges**
   - Link: https://www.codewars.com/
   - Try 8 kyu problems

3. **Python Principles**
   - Link: https://pythonprinciples.com/
   - Interactive beginner challenges

---

## 🐛 Common Issues & Troubleshooting

### Issue 1: "python: command not found"

**Solution:**
- Windows: Python not added to PATH. Reinstall and check "Add to PATH"
- Mac/Linux: Use `python3` instead of `python`
- Verify with: `where python` (Windows) or `which python` (Mac/Linux)

### Issue 2: VS Code doesn't recognize Python

**Solution:**
1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose your installed Python version
4. Restart VS Code

### Issue 3: Git commands not working

**Solution:**
- Windows: Restart computer after Git installation
- Verify installation: `git --version`
- Check if Git is in PATH

### Issue 4: Can't push to GitHub

**Solution:**
- Check internet connection
- Verify remote URL: `git remote -v`
- Try HTTPS instead of SSH (or vice versa)
- Check GitHub credentials

### Issue 5: Python script won't run

**Solution:**
- Check for syntax errors (red underlines in VS Code)
- Make sure file is saved (.py extension)
- Check Python interpreter is selected
- Try running from terminal: `python filename.py`

---

## 📊 Self-Assessment Quiz

Test your understanding:

1. **What command checks your Python version?**
   - Answer: `python --version` or `python3 --version`

2. **What are the four basic data types in Python?**
   - Answer: int (integer), float, str (string), bool (boolean)

3. **How do you create a variable in Python?**
   - Answer: `variable_name = value`

4. **What does the print() function do?**
   - Answer: Displays output to the console/terminal

5. **What is the difference between = and ==?**
   - Answer: = assigns a value, == compares values

6. **How do you add all files to Git staging?**
   - Answer: `git add .`

7. **What command commits your changes in Git?**
   - Answer: `git commit -m "message"`

8. **How do you create a comment in Python?**
   - Answer: Use # for single line, """ """ for multi-line

9. **What happens if you don't add Python to PATH?**
   - Answer: Command line won't recognize python command

10. **What's the keyboard shortcut to run Python in VS Code?**
    - Answer: Ctrl+Alt+N (with Code Runner) or Click Run button

---

## 📅 Tomorrow's Preview: Day 2

Get ready to learn:
- More about data types (strings, numbers, booleans)
- Operators (arithmetic, comparison, logical)
- String methods and manipulation
- Type conversion
- User input with input()
- Building interactive programs

**Preparation:**
- Review today's code
- Ensure all installations work
- Have questions ready
- Install requirement: None (we're all set!)

---

## 💭 Learning Journal

**Reflection Questions:**

1. What was the most challenging part of today?
   - _______________________

2. What concept do you feel confident about?
   - _______________________

3. What do you need to review?
   - _______________________

4. How many hours did you spend today?
   - _______________________

5. On a scale of 1-10, how well do you understand today's concepts?
   - _______________________

6. What question do you have for tomorrow?
   - _______________________

---

## ✅ Day 1 Completion Checklist

### Setup (Must Complete):
- [ ] Python 3.10+ installed and verified
- [ ] VS Code installed with Python extensions
- [ ] Git installed and configured
- [ ] GitHub account created
- [ ] SSH key added to GitHub (optional)

### Programming (Must Complete):
- [ ] Ran Python in REPL/interactive mode
- [ ] Created and ran hello.py
- [ ] Understand variables and assignment
- [ ] Know 4 basic data types
- [ ] Used print() function successfully
- [ ] Completed at least 2 practice exercises

### Git/GitHub (Must Complete):
- [ ] Initialized Git repository
- [ ] Created README.md
- [ ] Made first commit
- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Can view repository online

### Documentation:
- [ ] Took notes on key concepts
- [ ] Bookmarked important resources
- [ ] Filled out learning journal
- [ ] Identified tomorrow's goals

**Overall Completion: ____%**

---

## 🎉 Congratulations!

You've completed Day 1 of your AI career journey! You now have:
- A fully configured development environment
- Your first Python programs
- A GitHub repository to showcase your work
- Foundation for tomorrow's learning

**Remember:** Every expert was once a beginner. You're on the right path! 🚀

---

## 🔗 Quick Links Summary

**Software Downloads:**
- Python: https://www.python.org/downloads/
- VS Code: https://code.visualstudio.com/
- Git: https://git-scm.com/downloads
- GitHub: https://github.com/

**Documentation:**
- Python Docs: https://docs.python.org/3/
- VS Code Python: https://code.visualstudio.com/docs/python/python-tutorial
- Git Handbook: https://guides.github.com/introduction/git-handbook/

**Learning Resources:**
- Real Python: https://realpython.com/
- Python Tutor: https://pythontutor.com/
- W3Schools: https://www.w3schools.com/python/

---

**Day Status:** Day 1 of 168 (6 months × 28 days)
**Next:** [Day 2 - Data Types & Operators](./Day_02_Complete_Guide.md)

*Keep coding, keep learning! See you tomorrow! 💻*