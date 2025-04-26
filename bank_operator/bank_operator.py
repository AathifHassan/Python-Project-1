from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return  # Don't add the user to the list if the email is invalid.
    
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users found.")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    list_users()
    idx = int(input("Select user number: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user number!")
        return
    
    print("Account Type:")
    print("1. Savings Account")
    print("2. Student Account")
    print("3. Current Account")
    
    account_choice = int(input("Enter your choice (1, 2, 3): "))
    amount = float(input("Enter initial deposit: "))
    
    if amount <= 0:
        print("Invalid deposit amount!")
        return
    
    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid choice!")
        return
    
    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user number!")
        return
    
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    
    acc_idx = int(input("Select account: ")) - 1
    if acc_idx < 0 or acc_idx >= len(user.accounts):
        print("Invalid account selection!")
        return
    
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid deposit amount!")
        return
    
    user.accounts[acc_idx].deposit(amount)
    print("Deposit successful.\n")

def withdraw_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user number!")
        return
    
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    
    acc_idx = int(input("Select account: ")) - 1
    if acc_idx < 0 or acc_idx >= len(user.accounts):
        print("Invalid account selection!")
        return
    
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    
    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    if idx < 0 or idx >= len(users):
        print("Invalid user number!")
        return
    
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc
