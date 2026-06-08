def deposit_money(crsr, conn):
    acc_no = input("Account No: ")
    amount = int(input("Deposit Amount: "))
    dot = input("Date (YYYY-MM-DD): ")

    crsr.execute("UPDATE Account SET Balance = Balance + %s WHERE Acc_No=%s",
                 (amount, acc_no))

    crsr.execute("INSERT INTO Bank_Transaction VALUES (%s,%s,%s,%s)",
                 (acc_no, amount, dot, 'D'))

    conn.commit()
    print("✅ Money deposited successfully")


def withdraw_money(crsr, conn):
    acc_no = input("Account No: ")
    amount = int(input("Withdraw Amount: "))
    dot = input("Date (YYYY-MM-DD): ")

    crsr.execute("SELECT Balance FROM Account WHERE Acc_No=%s", (acc_no,))
    bal = crsr.fetchone()

    if bal and amount <= bal[0]:
        crsr.execute("UPDATE Account SET Balance = Balance - %s WHERE Acc_No=%s",
                     (amount, acc_no))

        crsr.execute("INSERT INTO Bank_Transaction VALUES (%s,%s,%s,%s)",
                     (acc_no, amount, dot, 'W'))

        conn.commit()
        print("✅ Withdrawal successful")
    else:
        print("❌ Insufficient balance or invalid account")


def display_all_transactions(crsr):
    crsr.execute("SELECT * FROM Bank_Transaction")
    for x in crsr:
        print(x)