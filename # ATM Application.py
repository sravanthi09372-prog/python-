# ATM Application

balance = 10000
pin = "1234"

print("===== Welcome to ATM =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
                print(f"New balance: ₹{balance}")
            else:
                print("Please enter a valid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Please enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                print(f"Remaining balance: ₹{balance}")

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN.")