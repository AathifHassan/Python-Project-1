from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from bank_operator import bank_operator
import time

console = Console()

def menu():
    while True:
        console.clear()

        table = Table(title="🏦 Bank System Menu", title_style="bold magenta")
        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "Deposit")
        table.add_row("5", "Withdraw")
        table.add_row("6", "View Transactions")
        table.add_row("7", "Exit")

        console.print(table)

        choice = Prompt.ask("👉 Choose option", choices=[str(i) for i in range(1, 8)], default="7")

        if choice == '1':
            bank_operator.create_user()
            time.sleep(2)  # Pause for 2 seconds before clearing
        elif choice == '2':
            bank_operator.list_users()
            input("\nPress Enter to go back to the menu.")  # Wait for user to press Enter before continuing
        elif choice == '3':
            bank_operator.create_account()
            time.sleep(2)
        elif choice == '4':
            bank_operator.deposit_money()
            time.sleep(2)
        elif choice == '5':
            bank_operator.withdraw_money()
            time.sleep(2)
        elif choice == '6':
            bank_operator.view_transactions()
            input("\nPress Enter to go back to the menu.")  # Pause for viewing transactions
        elif choice == '7':
            console.print("\n👋 Exiting... Thank you for using the Bank System!", style="bold green")
            break

if __name__ == "__main__":
    menu()

