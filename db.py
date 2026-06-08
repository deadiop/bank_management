import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',   
        charset='utf8',
        autocommit=False
    )

    crsr = conn.cursor()

    crsr.execute("CREATE DATABASE IF NOT EXISTS bharat_bank")
    crsr.execute("USE bharat_bank")

    crsr.execute("""
    CREATE TABLE IF NOT EXISTS Account (
        Acc_No VARCHAR(25),
        Name VARCHAR(25),
        DOB DATE,
        Mobile_no VARCHAR(25),
        Balance INT
    )
    """)

    crsr.execute("""
    CREATE TABLE IF NOT EXISTS Bank_Transaction (
        Acc_no VARCHAR(25),
        Amount INT,
        DOT DATE,
        Ttype CHAR(1)
    )
    """)

    crsr.execute("""
    CREATE TABLE IF NOT EXISTS credit (
        Acc_no VARCHAR(25),
        creditcard_no VARCHAR(16),
        DOT DATE,
        amount INT
    )
    """)

    crsr.execute("""
    CREATE TABLE IF NOT EXISTS loans (
        Acc_no VARCHAR(25),
        loan_amount FLOAT,
        loan_term INT,
        borrower_email VARCHAR(25),
        credit_score INT
    )
    """)

    conn.commit()
    return conn, crsr