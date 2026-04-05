# Expense Tracker

total = 0  

print("Enter your expenses one by one.")
print("Type 'done' when finished.\n")

while True:
    entry = input("Enter expense: ")

    if entry.lower() == 'done':
        break

    try:
        expense = float(entry)  # convert input to number
        total = total + expense  # accumulator logic
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

print("\nTotal Expense:", total)