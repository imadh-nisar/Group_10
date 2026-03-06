# Simple Budget Tracker with Multiple Expenses

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget (LKR): "))

# Initialize total expenses
total_expenses = 0.0

# Loop for multiple expenses
while True:
    expense = input("Enter an expense (or type 'done' to finish): ")

    # Check if user wants to stop
    if expense.lower() == "done":
        break

    # Add expense to total
    try:
        total_expenses += float(expense)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Calculate remaining balance
remaining = budget - total_expenses

# Display result
print("------------------------------")
print(f"Total Budget   : {budget:.2f} LKR")
print(f"Expenses Total : {total_expenses:.2f} LKR")
print(f"Remaining      : {remaining:.2f} LKR")

# Warning if funds are low
if remaining < 500:
    print("Warning: Low Funds")
print("------------------------------")