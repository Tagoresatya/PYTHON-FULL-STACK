def Zero_division_error_case():
    try:
        transactions = []
        average_transaction = sum(transctions)/ken(transactions)
        print("Avergae Transaction:",average_transaction)
    except ZeroDivisionError:
        print("Error:Cannot caluculate average transactions because there are not")
def value_error_case():
    try:
        withdrawl_amount = int("100/1")
        print("Withdrawing:", withdrawl_amount)
    except ValueError:
        print("Error: Invalid value entered. please enter a amount.")
def type_error():
    try:
        balance = 500
        deposit_amount = "100"
        new_balance = balance + deposit_amount
        print("New Balance",new_balance)
    except TypeError:
        print("Error: Incompitable data types cannot add string to an integer.")
def index_error_cse():
    try:
        transaction_history = [200,-150,300]
        print("Last transaction:",transaction_history[5])
    except IndexError:
        print("Error: trying to access a transaction that does not exist.")
def key_error_case():
    try:
        accounts = {"12345": {"pin":"1111"}", "balance":"1000"}
        account_number = "67890"
        print("Error:Account number not found.")

def file_not_found_error_case():
    try:
        with open("transaction_log.txt","r") as file:
            data = file.read()
    except FileNotFoundError:
        










while True:
    print("\n------ATM Simulation Menu-----")
    print("1.Check Average Transction(ZeroDivisionError) ")
    print("2.Withdarw with Invalid Input(valueError)")
    print("3.Deposit with Invlid Data Type(TypeError)")
    print("4.Access Invalid Transction History (IndexError)")
    print("5.Access Non-Existent Account (KeyError)")
    print("6.Read Missing Transaction Log File (FileNot FoundError)")
    print("7.Exit")

    if choice =="1":
        zero_division_error_case()
    elif choice == "2":
        value_error
