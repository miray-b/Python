import time

balance=1000
while True:
    print("\n" + "*"*20)
    print("ATM SYSTEM")
    print("1. Balance")
    print("2. Deposit")
    print("3. Whitdraw")
    print("4. Exit")

    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print(f" \n 💰 Current Balance: {balance} €")
    elif choice == "2":
        try:
            amount=int(input("Amount to deposit: "))
            if amount <= 0:
                print("❌Error: Please enter a positive value!")
            else:
                print("Waiting...")
                time.sleep(1)
                balance = balance + amount
                print(f"\n✅ Deposit Successful! New Balance: {balance} €")
        except ValueError:
            print("❌ Error: Please enter only numbers!")
    elif choice == "3":
        try:
            amount=int(input("Amount to whitdraw: "))
            if amount <=0:
                print("❌ Error: Please enter a positive value!")
            elif amount > balance:
                print("\n❌ Insufficient funds! (Yetersiz Bakiye)")
            else:
                print("Waiting...")
                time.sleep(1)
                balance= balance - amount
                print(f"\n✅ Withdrawal Successful! Remaining Balance: {balance} €")
        except ValueError:
            print("❌ Error: Please enter only numbers (numbers)!")
    elif choice == "4":
        print("Goodbye! See you later.")
        break
    else:
        print("Invalid choice! Please try again.")
    
