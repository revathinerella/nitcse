import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os
DATA_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_transactions():
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

transactions = load_transactions()

def update_balance():
    total = sum(t['amount'] for t in transactions)
    balance_label.config(text=f"Balance: ${total:.2f}")

def update_transaction_table():
    for item in transaction_table.get_children():
        transaction_table.delete(item)
    for t in transactions:
        transaction_table.insert("", "end", values=(
            t["date"],
            t["type"],
            t["category"],
            t["description"],
            f"${t['amount']:.2f}"
        ))

def clear_fields():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    trans_type.set("Expense")

def add_transaction():
    try:
        amount = float(amount_entry.get())
        if trans_type.get() == "Expense":
            amount = -abs(amount)
        else:
            amount = abs(amount)

        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": trans_type.get(),
            "category": category_entry.get(),
            "description": description_entry.get(),
            "amount": amount
        }

        transactions.append(transaction)
        save_transactions()
        update_transaction_table()
        update_balance()
        clear_fields()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for amount")

root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("700x500")

input_frame = ttk.Frame(root, padding=10)
input_frame.pack(fill="x")

ttk.Label(input_frame, text="Amount ($):").grid(row=0, column=0, sticky="w")
amount_entry = ttk.Entry(input_frame)
amount_entry.grid(row=0, column=1, padx=5)

ttk.Label(input_frame, text="Category:").grid(row=1, column=0, sticky="w")
category_entry = ttk.Entry(input_frame)
category_entry.grid(row=1, column=1, padx=5)

ttk.Label(input_frame, text="Description:").grid(row=2, column=0, sticky="w")
description_entry = ttk.Entry(input_frame)
description_entry.grid(row=2, column=1, padx=5)

trans_type = tk.StringVar(value="Expense")
ttk.Radiobutton(input_frame, text="Expense", variable=trans_type, value="Expense").grid(row=0, column=2)
ttk.Radiobutton(input_frame, text="Income", variable=trans_type, value="Income").grid(row=1, column=2)

ttk.Button(input_frame, text="Add Transaction", command=add_transaction).grid(row=2, column=2, padx=5, pady=10)

balance_label = ttk.Label(root, text="Balance: $0.00", font=("Arial", 16))
balance_label.pack(pady=10)

columns = ("Date", "Type", "Category", "Description", "Amount")
transaction_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    transaction_table.heading(col, text=col)
    transaction_table.column(col, anchor="center")

transaction_table.pack(fill="both", expand=True, padx=10, pady=10)

update_transaction_table()
update_balance()
root.mainloop()
