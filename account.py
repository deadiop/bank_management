def create_account(crsr, conn):
    print("\n--- CREATE ACCOUNT ---")

    acc_no = input("Account No: ")
    name = input("Name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    mobile = input("Mobile No: ")
    balance = int(input("Initial Deposit: "))

    crsr.execute(
        "INSERT INTO Account VALUES (%s,%s,%s,%s,%s)",
        (acc_no, name, dob, mobile, balance)
    )
    conn.commit()
    print("✅ Account created successfully!")


def display_account_details(crsr):
    acc_no = input("Enter Account No: ")

    crsr.execute("""
        SELECT Acc_No, Name, DOB, Mobile_no, Balance
        FROM Account WHERE Acc_No=%s
    """, (acc_no,))

    for i in crsr:
        print(i)


def display_all_account_info(crsr):
    crsr.execute("""
        SELECT Acc_No, Name, DOB, Mobile_no, Balance
        FROM Account
    """)

    for y in crsr:
        print(y)