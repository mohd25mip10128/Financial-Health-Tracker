# Separate file for budget data persistence
BUDGET_FILE = 'budget_core.txt'

def load_budget():
    """
    Loads budget data from the text file. Format: category,limit
    """
    budget_data = {}
    try:
        with open(BUDGET_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        budget_data[parts[0]] = float(parts[1])
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    return budget_data

def save_budget(budget_data):
    """
    Saves the current budget dictionary back to the text file.
    """
    with open(BUDGET_FILE, 'w') as f:
        for category, limit in budget_data.items():
            f.write(f"{category},{limit}\n")

def set_budget():
    """
    Allows the user to set or update a budget limit for a category.
    """
    budgets = load_budget()

    print("\n--- Set Monthly Budget ---")
    category = input("Enter category to set budget for (e.g., Food, Rent): ").strip().capitalize()

    while True:
        try:
            limit = float(input(f"Enter budget limit for {category}: "))
            if limit <= 0:
                 raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for the limit.")

    budgets[category] = limit
    save_budget(budgets)
    print(f"Budget for {category} set to ${limit:.2f}.")

def view_budget():
    """
    Displays all set budgets.
    """
    budgets = load_budget()
    if not budgets:
        print("\nNo budgets have been set yet.")
        return

    print("\n--- Current Budgets ---")
    print(f"{'Category':<15}{'Limit':<10}")
    print("-" * 25)
    for category, limit in budgets.items():
        print(f"{category:<15}${limit:.2f}")