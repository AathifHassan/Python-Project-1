from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if transaction_type not in ("deposit", "withdraw"):
            raise ValueError("Transaction type must be 'deposit' or 'withdraw'.")
        
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: ${self.amount}"
