# Financial Health Tracker (FHT)

## 🎯 Project Overview

The **Financial Health Tracker (FHT)** is a console-based Python application designed to help users log income, track expenses, and view essential financial analytics. This project demonstrates core programming concepts from the *CSE1021* syllabus.

**Key CSE1021 Concepts Applied:**

| Concept         | Implementation in FHT                                                                 |
|-----------------|-------------------------------------------------------------------------------------|
| Data Structures | Uses **lists** to store collections of data and **dictionaries** to model transactions and budget records |
| Algorithms      | Summation algorithm calculates totals (income, expenses); finding maximum identifies largest single expense |
| Control Flow    | **While loops** for the main menu, **if-elif-else** navigation, and **try-except** for validation |
| Data Persistence| Simple **file I/O** ensures reliability by saving and loading data between sessions  |

---

## 🛠️ Technical Design & Code Structure

All FHT logic resides in a single file (`fht_modular_core.py`) to ensure compactness. The code is organized into **five logical modules** (functions) for modularity and clarity:

| Module (Function)   | Role                                        |
|---------------------|---------------------------------------------|
| load_data, save_data| **Data Manager:** File I/O; convert plain text to Python dictionaries and back |
| add_transaction, view_transactions | **Transaction Handler:** Handles input, validation, and records management |
| generate_report     | **Reporting & Analytics:** Calculates net balance and spending breakdown         |
| handle_budget       | **Budgeting:** Sets and displays budget limits, saves budget info to file        |
| main                | **Main Control Flow:** Menu display, application loop, routing user choices      |

*To keep code simple and syllabus-aligned, modules such as `json`, `os`, `time`, and `datetime` are **not used**. Dates are entered as strings by users.*

---

## 🚀 Setup and Execution Instructions

### 1. Requirements

- **Python 3** (Any version)
- *No external libraries required*

### 2. File Setup

- Create a file named `fht_modular_core.py` in your working directory.
- Paste the complete code (see project source) into this file.

### 3. Execution Steps

1. Open your terminal or command prompt.
2. Navigate to the folder containing `fht_modular_core.py`.
3. Run the program:



---

## 📋 Usage Overview

The application lets you:
- Add new income or expense transactions.
- View all transactions.
- See summary reports including totals and largest expense.
- Set and display budget limits.

**All data is saved in plain text files—no extra setup is needed.**

---

## 📂 File Structure



---

## 💡 Notes and Constraints

- *No* use of `json`, `os`, `time`, or `datetime` for data handling.
- All dates are user-input as strings (e.g., `"2025-11-20"`).
- Code is organized for readability and modularity, fully commented and syllabus-compliant.

---

## 📊 Example

To add a transaction from Python code:
*Alternatively, use the interactive menu via terminal.*

---
## 💾 Data Persistence

The application will automatically create and manage two persistent plain text files in the execution directory to store data:

- **transactions.txt**  
  Stores transaction history in a CSV-like format.  
  Each line represents a transaction and contains:

