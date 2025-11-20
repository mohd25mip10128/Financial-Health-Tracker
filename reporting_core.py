def calculate_net_balance(transactions):
    """
    Calculates total income, total expenses, and the net balance.
    (Applies Summation Algorithm - Unit 3)
    """
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    net_balance = total_income - total_expense
    return total_income, total_expense, net_balance

def expense_breakdown(transactions):
    """
    Calculates the total expense for each category using a dictionary.
    (Applies Dictionaries and Iteration - Unit 5)
    """
    category_totals = {}
    expense_transactions = [t for t in transactions if t['type'] == 'expense']

    for t in expense_transactions:
        category = t['category']
        amount = t['amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    return category_totals

def find_max_expense(transactions):
    """
    Identifies the largest single expense transaction.
    (Applies Finding the Maximum number - Array Technique - Unit 5)
    """
    expense_transactions = [t for t in transactions if t['type'] == 'expense']
    if not expense_transactions:
        return None

    max_t = max(expense_transactions, key=lambda t: t['amount'])
    return max_t


def generate_financial_report(transactions):
    """
    Presents the full report to the user.
    """
    if not transactions:
        print("\nCannot generate report: No transactions recorded.")
        return

    total_income, total_expense, net_balance = calculate_net_balance(transactions)
    category_summary = expense_breakdown(transactions)
    max_expense_t = find_max_expense(transactions)

    print("\n========== Financial Health Report ==========")
    print(f"Total Income:  ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Net Balance:   ${net_balance:.2f} ({'Surplus' if net_balance >= 0 else 'Deficit'})")
    print("-" * 43)

    print("Expense Breakdown by Category:")
    for category, total in category_summary.items():
        percentage = (total / total_expense) * 100 if total_expense > 0 else 0
        print(f"  - {category:<15} : ${total:.2f} ({percentage:.1f}%)")

    if max_expense_t:
        print("\nLargest Expense Found:")
        print(f"  Amount: ${max_expense_t['amount']:.2f} | Category: {max_expense_t['category']} | Date: {max_expense_t['date']}")
    print("===========================================\n")