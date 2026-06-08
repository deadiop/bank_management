from db import get_connection
from account import create_account, display_account_details, display_all_account_info
from transactions import deposit_money, withdraw_money, display_all_transactions
from credit import credit_card
from loan import loan

conn, crsr = get_connection()

while True:
    print("""
==================================================
           🏦 BHARAT BANK SYSTEM
==================================================
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Display Account Details
5. Display All Transactions
6. Display All Accounts
7. Credit Card System
8. Loan System
9. Exit
==================================================
""")

    ch = int(input("Enter choice: "))

    if ch == 1:
        create_account(crsr, conn)

    elif ch == 2:
        deposit_money(crsr, conn)

    elif ch == 3:
        withdraw_money(crsr, conn)

    elif ch == 4:
        display_account_details(crsr)

    elif ch == 5:
        display_all_transactions(crsr)

    elif ch == 6:
        display_all_account_info(crsr)

    elif ch == 7:
        credit_card(crsr, conn)

    elif ch == 8:
        loan(crsr, conn)

    elif ch == 9:
        print("Thank you for using Bharat Bank 👋")
        break

    else:
        print("Invalid choice")