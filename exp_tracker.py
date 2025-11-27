import csv

FILENAME = "expenses.csv"

# Create the file if it doesn't exist
try:
    with open(FILENAME, "r") as file:
        pass
except FileNotFoundError:
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Bill/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("\nExpense added successfully!\n")


def view_expenses():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        print("\n------ ALL EXPENSES ------")
        for row in reader:
            print(row)
    print()


def search_by_category():
    category = input("Enter category to search: ")
    print(f"\n--- Expenses in {category} ---")

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[1].lower() == category.lower():
                print(row)
                found = True

    if not found:
        print("No expenses found in this category.\n")


def total_expense():
    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[2])
    print(f"\n Total Expense: ₹{total}\n")


def menu():
    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Total Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()

#git remote add origin https://github.com/PavithraDevi146/python_training.git
# git branch -M main
# git push -u origin main
