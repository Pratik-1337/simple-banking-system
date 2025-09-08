import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_balance(balance):
    print(f"Your Balance is ₹{balance}")
    time.sleep(3)
    clear()

def deposit():
    amount = float(input("Enter a amount to deposit: ₹"))
    if amount < 0:
        print("Invalid Amount")
        time.sleep(2)
        clear()
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: ₹"))
    if amount > balance:
        print("Not Enough Balance")
        time.sleep(1)
        print(f"Your Balance is {balance}")
        time.sleep(1)
        clear()
        return 0
    elif amount < 0:
        print("Amount must be greater than ₹0")
        return 0
    else:
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("---------- Welcome to the Bank ----------\n")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit\n")
        print("-----------------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount = deposit()
            balance += amount
            print(f"Deposited ₹{amount} to your account")
            time.sleep(1)
            print(f"Your Current Balance is ₹{balance}")
            time.sleep(2)
            clear()
        elif choice == "3":
            amount = withdraw(balance)
            balance -= amount
            print(f"Withdrawn ₹{amount} from your account")
            time.sleep(1)
            print(f"Your Current Balance is ₹{balance}")
            time.sleep(2)
            clear()
        elif choice == "4":
            is_running = False
            clear()
        else:
            print("Invalid Choice")

    print("Thank You! Have a Nice Day!")
    time.sleep(2)
    clear()

if __name__ == '__main__':
    main()