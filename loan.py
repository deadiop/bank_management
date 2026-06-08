def loan(crsr, conn):
    acc = input("Account No: ")
    amount = float(input("Loan Amount: "))
    term = int(input("Loan Term (months): "))
    email = input("Email: ")
    score = int(input("Credit Score: "))

    if score == 0:
        decision = "Approved" if amount <= 5000 else "Rejected"
    else:
        decision = "Approved" if score >= 700 else "Rejected"

    crsr.execute(
        "INSERT INTO loans VALUES (%s,%s,%s,%s,%s)",
        (acc, amount, term, email, score)
    )

    conn.commit()

    print("Loan Status:", decision)