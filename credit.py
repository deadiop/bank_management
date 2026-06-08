import time

def credit_card(crsr, conn):
    print("\n--- CREDIT CARD SYSTEM ---")
    print("1. Apply Credit Card")
    print("2. Show Statement")
    print("3. Show Total Purchase")
    print("4. Add Purchase")
    print("5. Pay Bill")

    ch = int(input("Enter choice: "))

    if ch == 1:
        acc = input("Account No: ")
        cno = input("Credit Card No: ")
        date = input("Date: ")
        amount = int(input("Amount: "))

        crsr.execute("INSERT INTO credit VALUES (%s,%s,%s,%s)",
                     (acc, cno, date, amount))
        conn.commit()
        print("✅ Credit card created")

    elif ch == 2:
        cno = input("Card No: ")

        crsr.execute("SELECT * FROM credit WHERE creditcard_no=%s", (cno,))
        for x in crsr:
            print(x)

    elif ch == 3:
        cno = input("Card No: ")

        crsr.execute("SELECT SUM(amount) FROM credit WHERE creditcard_no=%s", (cno,))
        print("Total:", crsr.fetchone()[0])

    elif ch == 4:
        acc = input("Account No: ")
        cno = input("Card No: ")
        date = input("Date: ")
        amount = int(input("Purchase Amount: "))

        crsr.execute("INSERT INTO credit VALUES (%s,%s,%s,%s)",
                     (acc, cno, date, amount))
        conn.commit()
        print("Added successfully")

    elif ch == 5:
        cno = input("Card No: ")

        crsr.execute("SELECT SUM(amount) FROM credit WHERE creditcard_no=%s", (cno,))
        total = crsr.fetchone()[0] or 0

        print("Total Due:", total)

        pay = int(input("Enter payment: "))
        date = time.strftime('%Y-%m-%d')

        crsr.execute("INSERT INTO credit VALUES (%s,%s,%s,%s)",
                     ("PAYMENT", cno, date, -pay))
        conn.commit()