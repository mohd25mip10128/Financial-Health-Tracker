# Define the file path for data persistence
DATA_FILE = 'transactions_core.txt'

def load_data():
    """
    Loads transactions from a simple CSV-like text file.
    Format: id,type,amount,category,date
    """
    transactions = []
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f:
                # Use split to separate the CSV fields
                parts = line.strip().split(',')
                if len(parts) == 5:
                    try:
                        transactions.append({
                            'id': int(parts[0]),
                            'type': parts[1],
                            'amount': float(parts[2]),
                            'category': parts[3],
                            # Date is loaded as a simple string
                            'date': parts[4]
                        })
                    except ValueError:
                        # Skip corrupted lines
                        continue
    except FileNotFoundError:
        pass
    return transactions

def save_data(transactions):
    """
    Saves the current list of transactions back to the text file.
    """
    with open(DATA_FILE, 'w') as f:
        for t in transactions:
            # Format transaction dictionary back into a CSV string
            line = f"{t['id']},{t['type']},{t['amount']},{t['category']},{t['date']}\n"
            f.write(line)