import requests

base_url = "http://127.0.0.1:8000"

# Function to call API endpoint
def call_api(endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

# Get all expenses
expenses = call_api("/expenses")
print("All Expenses")
for expense in expenses:
    print(expense["item"], "-", expense["amount"])

# Get the highest expense
highest_expense = call_api("/expenses/highest")
print(f"\nHighest Expense - item & amount:")
print(highest_expense["item"], "-", highest_expense["amount"])

# Normal way to call an API
def normal_api_call():
    url = "http://127.0.0.1:8000/expenses/highest"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    if response.status_code == 200:
        h_expense = response.json()
        print("\nStatus code:", response.status_code)
        print("Highest Expenses - called using a normal api call:")
        print(h_expense["item"], "-", h_expense["amount"])
    else:
        print("\nSomething went wrong. Check if your API server is running!")

normal_api_call()