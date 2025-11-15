# Day 7: Week 1 Capstone Project - Personal Finance Manager

**Duration:** 6-8 hours | **Date:** _________ | **Status:** ⬜ Not Started | ⬜ In Progress | ⬜ Completed

---

## 🎯 Project Overview

**Project Name:** Personal Finance Tracker & Budget Manager

**Description:**
Build a comprehensive personal finance application that tracks income, expenses, budgets, and provides financial insights. This project will integrate ALL concepts learned in Week 1 (Days 1-6).

**Why This Project?**
- Real-world application everyone can use
- Covers all fundamental Python concepts
- Demonstrates data management skills
- Portfolio-worthy project
- Extensible for future features

---

## 🎓 Learning Objectives

By completing this project, you will demonstrate mastery of:

### Day 1-2 Concepts:
- ✅ Variables and data types
- ✅ Operators (arithmetic, comparison, logical)
- ✅ String manipulation and formatting
- ✅ Type conversion
- ✅ User input handling

### Day 3 Concepts:
- ✅ If/elif/else statements
- ✅ Nested conditionals
- ✅ Complex boolean logic
- ✅ Input validation

### Day 4 Concepts:
- ✅ For loops for iteration
- ✅ While loops for menus
- ✅ Break and continue
- ✅ Nested loops

### Day 5 Concepts:
- ✅ Function definition and calling
- ✅ Parameters and return values
- ✅ Default parameters
- ✅ Scope management
- ✅ Modular code organization

### Day 6 Concepts:
- ✅ Lists for data storage
- ✅ List comprehensions
- ✅ Sorting and filtering
- ✅ Tuples for immutable data
- ✅ List methods

---

## 📋 Project Requirements

### Core Features (Must-Have):

1. **Transaction Management**
   - Add income transactions
   - Add expense transactions
   - View all transactions
   - Delete transactions
   - Edit transactions
   - Search transactions

2. **Category Management**
   - Predefined expense categories (Food, Transport, Bills, etc.)
   - Custom category creation
   - Category-based filtering

3. **Budget System**
   - Set monthly budgets per category
   - Track spending against budget
   - Budget alerts when approaching/exceeding limit

4. **Reporting & Analytics**
   - Monthly expense summary
   - Income vs Expense comparison
   - Category-wise breakdown
   - Spending trends
   - Savings calculation

5. **Data Persistence (Basic)**
   - Save data to text file (simple CSV format)
   - Load data on startup

### Bonus Features (Optional):

6. **Advanced Analytics**
   - Year-to-date statistics
   - Month-over-month comparison
   - Top spending categories
   - Average daily spending

7. **Goal Tracking**
   - Set savings goals
   - Track progress toward goals
   - Projected completion date

8. **Export Features**
   - Generate text-based reports
   - Export transactions to file

---

## 🏗️ Project Architecture

### Data Structures

**Transaction (Dictionary):**
```python
transaction = {
    'id': unique_id,          # int
    'type': 'income/expense', # string
    'amount': 100.50,         # float
    'category': 'Food',       # string
    'description': 'Grocery', # string
    'date': '2024-01-15',    # string (YYYY-MM-DD)
}
```

**Budget (Dictionary):**
```python
budget = {
    'category': 'Food',     # string
    'limit': 500.00,        # float
    'month': '2024-01'      # string (YYYY-MM)
}
```

**Main Data Containers:**
- `transactions` - List of transaction dictionaries
- `budgets` - List of budget dictionaries
- `categories` - List of category strings
- `monthly_income` - Float tracking current month income
- `monthly_expenses` - Float tracking current month expenses

### Function Structure

Your program should be organized into logical function groups:

**1. Main Program Functions:**
- `main()` - Main program loop
- `display_main_menu()` - Show menu options
- `handle_menu_choice()` - Process user selection

**2. Transaction Functions:**
- `add_income()` - Record income
- `add_expense()` - Record expense
- `view_transactions()` - Display all transactions
- `delete_transaction()` - Remove transaction
- `edit_transaction()` - Modify transaction
- `search_transactions()` - Find specific transactions

**3. Budget Functions:**
- `set_budget()` - Create/update budget
- `view_budgets()` - Display all budgets
- `check_budget_status()` - Compare spending vs budget
- `get_budget_alerts()` - Warn about budget limits

**4. Analytics Functions:**
- `calculate_monthly_summary()` - Monthly totals
- `get_category_breakdown()` - Spending by category
- `calculate_savings()` - Income - Expenses
- `get_spending_trend()` - Weekly/monthly patterns

**5. Utility Functions:**
- `validate_amount()` - Ensure valid number input
- `validate_date()` - Check date format
- `format_currency()` - Display money properly
- `get_current_month()` - Return current month string
- `generate_transaction_id()` - Create unique ID

**6. File I/O Functions:**
- `save_data()` - Write to file
- `load_data()` - Read from file

---

## 🚀 Implementation Guide

### Phase 1: Project Setup (30 minutes)

**Step 1: Create Project Structure**

Create a file: `finance_tracker.py`

**Step 2: Define Initial Data Structures**

Think about:
- What variables do you need globally?
- What data structures will hold your transactions?
- What categories should be predefined?

**Step 3: Create Basic Menu**

Implement:
- Display main menu function
- Basic while loop for program flow
- Exit option

**Questions to Consider:**
- How will you handle invalid menu selections?
- Should the menu be numbered or letter-based?
- What's the best way to keep the program running until user exits?

---

### Phase 2: Transaction Management (2 hours)

**Step 1: Add Income Function**

Requirements:
- Prompt user for amount (validate it's a positive number)
- Ask for description
- Ask for date (or use today's date)
- Assign category as "Income"
- Generate unique transaction ID
- Add to transactions list
- Show confirmation message

**Challenges to Solve:**
- How do you validate the amount is a valid positive number?
- How do you handle invalid input without crashing?
- What's the best way to generate unique IDs?
- How do you get today's date in Python?

**Hints:**
- Use try-except for number validation
- Use a counter or timestamp for IDs
- Look into the `datetime` module for dates
- Create a helper function for amount validation

**Step 2: Add Expense Function**

Requirements:
- Similar to add_income but for expenses
- Must select from available categories
- Validate category exists
- Calculate running total

**Additional Challenges:**
- How do you display categories for user to choose?
- Should you allow custom categories?
- How do you ensure user picks a valid category?

**Step 3: View Transactions**

Requirements:
- Display all transactions in a formatted table
- Show: ID, Date, Type, Category, Amount, Description
- Calculate and show totals at the bottom
- Handle empty transaction list

**Display Considerations:**
- How wide should each column be?
- How do you align text nicely?
- Should you use colors or symbols for income vs expense?
- What's the best way to format currency?

**Example Output Format:**
```
================================================================================
                           TRANSACTION HISTORY
================================================================================
ID    Date        Type      Category      Amount      Description
--------------------------------------------------------------------------------
1     2024-01-15  Income    Salary        $2,500.00   Monthly salary
2     2024-01-16  Expense   Food          $45.50      Groceries
3     2024-01-17  Expense   Transport     $30.00      Gas
================================================================================
Total Income:  $2,500.00
Total Expense: $75.50
Net Balance:   $2,424.50
================================================================================
```

**Step 4: Delete Transaction**

Requirements:
- Display all transactions
- Ask user for transaction ID to delete
- Confirm deletion
- Remove from list
- Update totals

**Considerations:**
- How do you find a transaction by ID?
- What if the ID doesn't exist?
- Should you ask for confirmation?
- How do you remove an item from a list?

**Step 5: Search Transactions**

Requirements:
- Search by category
- Search by date range
- Search by description keyword
- Display matching results

**Search Challenges:**
- How do you implement multiple search criteria?
- Should search be case-sensitive?
- How do you handle date range comparisons?
- What if no matches are found?

---

### Phase 3: Budget Management (1.5 hours)

**Step 1: Set Budget Function**

Requirements:
- Select category
- Enter budget amount
- Specify month (default to current month)
- Store in budgets list
- Handle updating existing budget

**Implementation Questions:**
- How do you check if a budget already exists for a category?
- Should you allow budget for multiple months?
- How do you structure the budget dictionary?

**Step 2: View Budgets**

Requirements:
- Display all budgets for current month
- Show: Category, Budget Limit, Spent, Remaining, Status
- Use color/symbols for status (under/over budget)

**Calculations Needed:**
- How do you calculate total spent per category?
- How do you filter transactions by month and category?
- What's the best way to show percentage used?

**Example Output:**
```
================================================================================
                        BUDGET STATUS - January 2024
================================================================================
Category      Budget      Spent       Remaining   Status
--------------------------------------------------------------------------------
Food          $500.00     $245.50     $254.50     ✓ 49%
Transport     $200.00     $180.00     $20.00      ⚠ 90%
Bills         $800.00     $820.00     -$20.00     ✗ Over!
Entertainment $150.00     $45.00      $105.00     ✓ 30%
================================================================================
```

**Step 3: Budget Alerts**

Requirements:
- Check spending against budgets
- Alert when 80% of budget used
- Alert when budget exceeded
- Display alerts when program starts

**Alert Logic:**
- When should you check budgets?
- How do you prevent showing the same alert multiple times?
- What threshold percentages should trigger warnings?

---

### Phase 4: Analytics & Reporting (2 hours)

**Step 1: Monthly Summary**

Requirements:
- Total income for current month
- Total expenses for current month
- Net savings (income - expenses)
- Breakdown by category
- Average daily spending

**Calculation Challenges:**
- How do you filter transactions by current month?
- How do you group expenses by category?
- How do you calculate number of days in current month?
- What if there's no data for current month?

**Step 2: Category Breakdown**

Requirements:
- Show spending per category
- Calculate percentage of total spending
- Sort by amount (highest to lowest)
- Display as table and/or simple bar chart

**Visualization Ideas:**
- Can you create a text-based bar chart?
- How do you calculate percentage of total?
- Should you show only top N categories?

**Example Text Chart:**
```
Category Spending Breakdown:
Food          ████████████████████ $450.00 (35%)
Transport     ████████████ $300.00 (23%)
Bills         ██████████ $250.00 (19%)
Entertainment ████ $100.00 (8%)
Other         ███ $75.00 (6%)
```

**Step 3: Spending Trends**

Requirements:
- Compare this month vs last month
- Show increase/decrease percentage
- Identify highest spending day
- Calculate average transaction size

**Trend Analysis:**
- How do you compare two time periods?
- How do you calculate percentage change?
- What if previous month has no data?

---

### Phase 5: Data Persistence (1.5 hours)

**Step 1: Save to File**

Requirements:
- Save all transactions to text file
- Save all budgets to text file
- Use simple format (CSV or custom)
- Overwrite file on each save

**File Format Considerations:**
- Should you use CSV, JSON, or custom format?
- How do you handle special characters in descriptions?
- Should transactions and budgets be in same or separate files?

**Simple CSV Format Example:**
```
# transactions.txt
id,type,amount,category,description,date
1,income,2500.00,Salary,Monthly salary,2024-01-15
2,expense,45.50,Food,Groceries,2024-01-16
```

**Step 2: Load from File**

Requirements:
- Read data when program starts
- Parse file contents
- Populate data structures
- Handle missing or corrupted files

**Error Handling:**
- What if file doesn't exist? (first run)
- What if file is corrupted?
- How do you convert string amounts back to floats?
- How do you handle empty lines?

**Step 3: Auto-Save**

Requirements:
- Save data after every transaction
- Save data on program exit
- Ensure data integrity

**Implementation Approach:**
- Should you save after every change?
- Or only on exit?
- How do you ensure save happens even if program crashes?

---

### Phase 6: User Interface & Polish (1 hour)

**Step 1: Improve Menu System**

Enhancements:
- Add clear screen functionality
- Add "Press Enter to continue" pauses
- Add header/banner
- Color code different sections (optional)

**Step 2: Input Validation**

Ensure validation for:
- All numeric inputs (amounts, IDs)
- Date inputs (format checking)
- Menu selections
- Empty inputs

**Validation Pattern:**
```python
def get_valid_amount(prompt):
    """Get and validate amount input"""
    # Keep asking until valid
    # Return float value
    pass
```

**Step 3: Error Messages**

Provide helpful messages for:
- Invalid input
- Empty data scenarios
- File errors
- Budget exceeded warnings
- Success confirmations

**Step 4: Help System**

Add:
- Instructions for first-time users
- Tips for using features
- Command reference

---

## 🎯 Development Workflow

### Recommended Order:

**Week Plan:**

**Day 7 - Core Structure (6-8 hours):**
1. Set up project file and basic structure (30 min)
2. Implement menu system (30 min)
3. Build add_income function (45 min)
4. Build add_expense function (45 min)
5. Build view_transactions function (1 hour)
6. Test basic CRUD operations (30 min)
7. Implement delete_transaction (45 min)
8. Implement search_transactions (1 hour)
9. Set up basic budgets (1 hour)
10. Test all features (30 min)

**Bonus Time (if you have more time):**
- Add file I/O (1 hour)
- Add analytics (1 hour)
- Add budget alerts (45 min)
- Polish UI (45 min)

---

## 🧪 Testing Checklist

### Functional Testing:

**Transaction Management:**
- [ ] Can add income successfully
- [ ] Can add expense successfully
- [ ] Invalid amount is rejected
- [ ] Transactions display correctly
- [ ] Can delete transaction
- [ ] Delete handles invalid ID
- [ ] Can search by category
- [ ] Can search by date
- [ ] Empty transaction list handled

**Budget System:**
- [ ] Can set budget for category
- [ ] Budget updates correctly
- [ ] Budget alerts work
- [ ] Over-budget shows warning
- [ ] Budget calculations accurate

**Analytics:**
- [ ] Monthly summary calculates correctly
- [ ] Category breakdown accurate
- [ ] Percentages add to 100%
- [ ] Handles no data gracefully

**Data Persistence:**
- [ ] Data saves to file
- [ ] Data loads from file
- [ ] Handles missing file
- [ ] Handles corrupted data

**User Interface:**
- [ ] Menu displays properly
- [ ] Invalid menu choice handled
- [ ] All prompts clear
- [ ] Numbers format as currency
- [ ] Tables align properly

---

## 💡 Problem-Solving Hints

### Common Challenges & Approaches:

**Challenge 1: Generating Unique IDs**

Problem: How to ensure each transaction has a unique ID?

Approaches to Consider:
- Use a counter variable
- Use timestamp
- Use length of list + 1
- UUID library (advanced)

Which is best and why?

**Challenge 2: Filtering by Month**

Problem: How to get only transactions from current month?

Approaches:
- Store month separately in transaction
- Parse date string and compare
- Use datetime module
- Keep separate monthly lists

Think about pros/cons of each.

**Challenge 3: Calculating Category Totals**

Problem: Sum all expenses for a specific category.

Approaches:
- Loop through all transactions and sum
- Use list comprehension
- Keep running totals
- Use dictionary to track

Which is most efficient?

**Challenge 4: Validating Numeric Input**

Problem: User enters non-numeric value for amount.

Solution Pattern:
```python
def get_valid_amount():
    while True:
        # Get input
        # Try to convert to float
        # If error, ask again
        # If negative, ask again
        # If valid, return
        pass
```

**Challenge 5: Formatting Tables**

Problem: Making data align in columns.

Consider:
- Fixed-width formatting with f-strings
- Dynamic column width based on content
- Separator lines
- Headers and footers

Example Approach:
```python
# How would you make this align?
print(f"{'ID':<5} {'Date':<12} {'Amount':>10}")
```

---

## 📚 Concepts to Review Before Starting

### Essential Concepts:

**Dictionaries** (You'll use them heavily):
```python
# You'll need to work with dictionaries
transaction = {'id': 1, 'amount': 100.50, 'type': 'expense'}
# How do you access values?
# How do you modify values?
# How do you check if key exists?
```

**List of Dictionaries:**
```python
# Your main data structure
transactions = [
    {'id': 1, 'amount': 100.50},
    {'id': 2, 'amount': 50.00}
]
# How do you find a specific transaction?
# How do you delete a transaction?
# How do you update a transaction?
```

**String Formatting:**
```python
# You'll need currency formatting
amount = 1234.56
print(f"${amount:.2f}")  # $1234.56
print(f"${amount:,.2f}") # $1,234.56
```

**Date Handling:**
```python
# Getting today's date
from datetime import datetime
today = datetime.now()
date_string = today.strftime("%Y-%m-%d")
```

---

## 🎨 Example User Flow

### Typical Session:

```
================================================================================
                    PERSONAL FINANCE TRACKER
================================================================================
Welcome back! You have 15 transactions totaling $2,500.00

⚠️ BUDGET ALERT: Food category at 90% ($450/$500)

================================================================================
                           MAIN MENU
================================================================================
1. Add Income
2. Add Expense
3. View Transactions
4. Manage Budgets
5. View Reports
6. Search Transactions
7. Settings
8. Exit
================================================================================
Select option: 2

--- ADD EXPENSE ---

Categories:
1. Food
2. Transport
3. Bills
4. Entertainment
5. Shopping
6. Health
7. Other
8. Create New Category

Select category (1-8): 1

Amount: $45.50
Description: Lunch at cafe
Date (YYYY-MM-DD) or press Enter for today: [Enter]

✓ Expense added successfully!
  Category: Food
  Amount: $45.50
  Date: 2024-01-15

⚠️ Food budget now at 95% ($495.50/$500.00)

Press Enter to continue...
```

---

## 🏆 Success Criteria

### Minimum Viable Product (MVP):

Your project should have:
- ✅ At least 10 working functions
- ✅ Transaction CRUD operations (Create, Read, Update, Delete)
- ✅ Basic budget system
- ✅ Monthly summary report
- ✅ Menu-driven interface
- ✅ Input validation
- ✅ Proper use of all Week 1 concepts

### Code Quality Standards:

- ✅ Functions have docstrings
- ✅ Meaningful variable names
- ✅ Proper indentation
- ✅ Comments for complex logic
- ✅ No global variable abuse
- ✅ Error handling present
- ✅ Code organized logically

---

## 📈 Extension Ideas

### If you finish early:

**Level 1 Extensions:**
- Recurring transactions (auto-add monthly bills)
- Multiple user accounts
- Password protection
- Backup system

**Level 2 Extensions:**
- Export to CSV
- Import from CSV
- Data visualization (more advanced charts)
- Savings goals tracker

**Level 3 Extensions:**
- Web interface (later in course)
- Database integration (later in course)
- Email reports
- API integration for exchange rates

---

## 🤔 Reflection Questions

### After Completing the Project:

1. **What was the most challenging part?**
   - Why was it challenging?
   - How did you overcome it?

2. **Which Week 1 concept did you use most?**
   - Lists? Functions? Loops? Conditionals?

3. **What would you do differently if starting over?**
   - Better planning?
   - Different data structures?
   - Different function organization?

4. **What feature are you most proud of?**
   - Why does it stand out?

5. **What did you learn that wasn't explicitly taught?**
   - Problem-solving approaches?
   - Python features you discovered?

---

## 📝 Documentation Requirements

### Your project should include:

**1. README.md File:**
```markdown
# Personal Finance Tracker

## Description
[What your program does]

## Features
- Feature 1
- Feature 2
...

## How to Run
1. Step 1
2. Step 2

## Usage Examples
[Screenshots or examples]

## Technologies Used
- Python 3.x
- [Any modules]

## Future Enhancements
[What you'd add next]
```

**2. Code Comments:**
- Function docstrings
- Complex logic explained
- TODO notes for incomplete features

**3. User Guide:**
- How to use each feature
- Tips and tricks
- Troubleshooting common issues

---

## 🎓 Learning Outcomes

### By completing this project, you demonstrate:

**Technical Skills:**
- ✅ Python fundamentals mastery
- ✅ Data structure selection
- ✅ Algorithm implementation
- ✅ Problem decomposition
- ✅ Error handling
- ✅ File I/O

**Soft Skills:**
- ✅ Project planning
- ✅ Problem-solving
- ✅ Debugging
- ✅ Documentation
- ✅ User experience thinking

**Portfolio Value:**
- ✅ Real-world application
- ✅ Complete project
- ✅ Demonstrates range of skills
- ✅ Extensible codebase
- ✅ Professional presentation

---

## 🚀 Getting Started Checklist

Before you begin coding:

- [ ] Read entire project guide
- [ ] Understand all requirements
- [ ] Review Week 1 concepts (Days 1-6)
- [ ] Set up project file
- [ ] Plan your function structure
- [ ] Decide on data structures
- [ ] Create a development timeline
- [ ] Prepare test data

**Now you're ready to build!** 🎉

---

## 💪 Motivation

This project represents everything you've learned in your first week of Python. It's challenging, but you have all the skills needed to complete it.

Remember:
- Break it into small pieces
- Test frequently
- Don't aim for perfection first time
- Google and ask questions
- Iterate and improve

**You've got this!** 💻

---

## 📞 Getting Help

### When you're stuck:

**1. Review the relevant day's guide**
- Day 5 for function issues
- Day 6 for list problems
- Day 3 for conditional logic

**2. Debugging strategies:**
- Print statements everywhere
- Test functions individually
- Use simple test data
- Comment out complex parts

**3. Resources:**
- Python documentation
- Previous day examples
- Stack Overflow
- Python communities (Reddit, Discord)

**4. Break time:**
- Step away for 15 minutes
- Explain problem out loud
- Draw the logic on paper
- Try a different approach

---

## ✅ Project Submission Checklist

### Before considering it complete:

- [ ] All core features working
- [ ] Code is commented
- [ ] README.md created
- [ ] Tested with various inputs
- [ ] Tested error conditions
- [ ] Code is organized
- [ ] Variable names are clear
- [ ] Functions have docstrings
- [ ] No obvious bugs
- [ ] Committed to GitHub
- [ ] Can explain how it works

---

**Project Status:** Day 7 Capstone  
**Estimated Time:** 6-8 hours  
**Difficulty:** Intermediate  
**Week:** 1 of 24  

🎉 **This is your first major milestone. Make it count!** 🎉

---

*"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie*

**Good luck! You're going to build something amazing!** 🚀