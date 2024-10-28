balance_amount=1000
while True:
    print("\n1.\tCheck balance")
    print("2.\tDeposit money")
    print("3.\tWithdraw money")
    print("4.\tExit")
    choice=int(input("enter you choice:"))
    if choice==1:
        print(f"the current balance${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("enter the amount"))
        balance_amount=balance_amount+deposit_amount
        print(f"the deposited amount${deposit_amount} and the current balance${balance_amount}")
    elif choice==3:
        withdraw_amount=float(input("enter the amount to withdraw"))
        if withdraw_amount>balance_amount:
            print("insufficient balance")
        else:
            balance_amount=balance_amount-withdraw_amount
            print(f"the amount withdraw from the account${withdraw_amount} the balance_amount${balance_amount}")
    if choice==4:
        break
    else:
        print("invalid entry")