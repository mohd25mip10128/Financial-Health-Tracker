# Import the core modules
from data_manager_core import load_data
from transaction_handler_core import add_transaction, view_transactions
from reporting_core import generate_financial_report
from budgeting_core import set_budget, view_budget

def display_menu():
    """
    Displays the main application menu.
    """
    print("\n--- Financial Health Tracker (FHT) Menu ---")
    print("1. Add New Transaction (Income/Expense)")
    print("2. View All Transactions")
    print("3. Generate Financial Report")
    print("4. Set/View Budget")
    print("5. Exit")
    print("-" * 43)

def main():
    """
    Main loop to run the FHT application.
    (Applies Conditional and Iteration statements - Unit 3)
    """
    # 1. Load existing data
    transactions = load_data()

    print("Welcome to the Financial Health Tracker!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            generate_financial_report(transactions)
        elif choice == '4':
            set_budget()
            view_budget()
        elif choice == '5':
            print("Thank you for using FHT. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()