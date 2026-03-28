def show_menu():
    print('\n=== SMART EXPENSE TRACKER ===')
    print('1. Add Expense')
    print('2. View all Expenses')
    print('3. Expense Summary')
    print('4. Exit')

def add_expense():
    date = input('Enter date (YYYY-MM-DD): ')
    amount = float(input('Enter amount: '))
    category = input('Enter category: ')
    description = input('Enter description: ')

    expense = {
        'date' : date,
        'amount': amount,
        'category': category,
        'description': description
        }
    return expense

def save_expense(expense):
    with open('expenses.csv', 'a') as file:
        line = f'{expense["date"]},{expense["amount"]},{expense["category"]},{expense["description"]}\n'
        file.write(line)

def view_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

            if len(lines) <= 1:
                print("No expenses recorded yet.")
                return
            
            print("\n--- ALL EXPENSES ---")
            print(f"{'Date':<12} {'Amount':<10} {'Category':<12} {'Description':<15}")
            print("-" * 55)

            for line in lines[1:]:
                date, amount, category, description = line.strip().split(",")
                print(f"{date:<12} {amount:<10} {category:<12} {description:<15}")

    except FileNotFoundError:
        print("Expense file not found.")

def expense_summary():
    try:
        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

            if len(lines) <= 1:
                print("No expenses recorded yet")
                return
        
        category_totals = {}

        for line in lines[1:]:
            date, amount, category, description = line.strip().split(",")
            amount = float(amount)

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

            print("\n--- EXPENSE SUMMARY ---")
            for category, total in category_totals.items():
                print(f"{category} : ₹{total}")

    except FileNotFoundError:
        print("Expense file not found.")

while True:
    show_menu()
    choice = input('Select an option(1-4): ')

    if choice == '1':
        expense = add_expense()
        save_expense(expense)
        print('Expense saved successfully.')

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        print('Expense Summary Selected')

    elif choice == '4':
        print('Exiting Program...')
        break
    else:
        print('Invalid choice. Try again.')





