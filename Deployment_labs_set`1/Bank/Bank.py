from flask import Flask, render_template, request

app = Flask(__name__)

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

# Initialize a bank account for demonstration
sample_account = BankAccount("12345")

@app.route('/')
def index():
    return render_template('index.html', balance=sample_account.balance)

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.form['amount'])
    message = sample_account.deposit(amount)
    return render_template('index.html', message=message, balance=sample_account.balance)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = float(request.form['amount'])
    message = sample_account.withdraw(amount)
    return render_template('index.html', message=message, balance=sample_account.balance)

if __name__ == '__main__':
    app.run(debug=True)
