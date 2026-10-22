from fastapi import FastAPI

app = FastAPI()

# API endpoint
@app.get("/")
def home():
    return {"message": "Hello! My API is working."}

# An endpoint to return expenses
@app.get("/expenses")
def get_expenses():
    return [
        {"item": "Groceries", "amount": 450},
        {"item": "Transport", "amount": 120},
        {"item": "Books", "amount": 600}
    ]

# Endpoint to return highest expense
@app.get("/expenses/highest")
def get_highest_expense():
    expenses = [
        {"item": "Groceries", "amount": 450},
        {"item": "Transport", "amount": 120},
        {"item": "Books", "amount": 600}
    ]

    return max(expenses, key=lambda expense: expense["amount"])