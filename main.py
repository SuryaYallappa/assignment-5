balance =0
kyc_documents = {}

def check_balance():
    print(f"Your Balance is {balance} $")
    print("=========================")

def deposit(amount):
    global balance
    if amount>0:
        balance += amount
    else:
        print("You can't deposit 0 or negitive ammount.")
        print("=========================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("You can't withdraw 0 or negitive ammount.")
    elif amount > balance:
        print("can not withdraw money more than your balance.")
        print("=========================")
    else:
        balance -= amount
        print("=========================")

def update_kyc(doc):
    global kyc_documents
    kyc_documents.update(doc)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("========================")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

if __name__ == "__main__":
    print("=========================")
    print("Welcome to ATM!")
    print("=========================")
    print()

    while True:
        print("1.Check Balance")
        print("2.Deposit Amount")
        print("3.Withdraw Amount")
        print("4.Check KYC")
        print("5.Update KYC")
        print("6.Exit")
        choice=input("Enter your choice(1-6): ")
        print("=========================")

        if choice=="1":
            check_balance()
        elif choice=="2":
            num = int(input("Enter your Deposit Amount:"))
            deposit(num)
            print(f"{num}$ deposited successfully!")
        elif choice=="3":
            num = int(input("Enter your withdraw Amount:"))
            withdraw(num)
            print(f"{num}$ withdrawen successfully!")
        elif choice=="4":
            check_kyc()
        elif choice=="5":
            docs=int(input("Enter the number documents you want to add : "))
            for doc in range(docs):
                key=input("Enter the document type:")
                value=input("Enter the document number:")
                kyc_documents[key]=value
            update_kyc(kyc_documents)

        elif choice=="6":
            break
        else:
            print("Invalid choice(select between 1-6)")
            print("=========================")

    print()
    print("Thank You For Using ATM")
