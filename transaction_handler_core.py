from data_manager_core import save_data, load_data

TRANSACTION_CATEGORIES = {
    'income': ['Salary', 'Gift', 'Investment'],
    'expense': ['Food', 'Rent', 'Travel', 'Utilities', 'Miscellaneous']
}

def add_transaction(transactions):
    """
    Allows the user to add a new income or expense transaction.
    """
    print("\n--- Add New Transaction ---")
    while True:
        type_choice = input("Enter type (i for Income, e for Expense): ").lower()
        if type_choice in ['i', 'e']:
            transaction_type = 'income' if type_choice == 'i' else 'expense'
            break
        print("Invalid choice. Please enter 'i' or 'e'.")

    # Amount input with error handling (Error Handling Strategy NFR)
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                 raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for the amount.")

    print(f"Available Categories for {transaction_type}: {', '.join(TRANSACTION_CATEGORIES[transaction_type])}")
    category = input("Enter category: ").strip()
    
    # MANUAL DATE INPUT (since no date/time modules are allowed)
    date_str = input("Enter date (e.g., YYYY-MM-DD): ").strip()

    next_id = max((t['id'] for t in transactions), default=0) + 1

    new_transaction = {
        'id': next_id,
        'type': transaction_type,
        'amount': amount,
        'category': category.capitalize(),
        'date': date_str # Date is the user-provided string
    }

    transactions.append(new_transaction)
    save_data(transactions)
    print("Transaction added successfully.")


def view_transactions(transactions):
    """
    Displays all recorded transactions. (Applies Iteration statements)
    """
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    print("\n--- All Transactions ---")
    print(f"{'ID':<4}{'Type':<10}{'Amount':<12}{'Category':<15}{'Date':<10}")
    print("-" * 51)
    for t in transactions:
        print(f"{t['id']:<4}{t['type'].capitalize():<10}${t['amount']:<11.2f}{t['category']:<15}{t['date']:<10}")