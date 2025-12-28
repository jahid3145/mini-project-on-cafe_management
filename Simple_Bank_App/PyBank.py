'''
PyBank -Simple banking app


#Features

1.Deposit money(support Decimal amount)
2.Withdraw money(cannot exceed availabe balance)
3.Check current balance
4.View transactions history
5.Show total deposits and withdrawals
6.Menu-based navigation with confirmation messages
7.Exit option to close the program

'''

balance =0.0
transaction =[]

def Deposit(amount):
    global balance
    
    balance += amount
    transaction.append(f'Deposited {amount}/-')
    print(f'{amount} Deposited Successfully\n')
    
def Withdraw(amount):
    global balance
    
    if amount > balance:
        print("Insufficent Balance")
    else:
        balance -= amount
        transaction.append(f'Withdrawn {amount}/-')
        print(f'{amount} Withdrawn Successfully\n')
    
def CheckBalance():
    print(f'Current Balance:{balance}\n')
    

def View_Transaction_History():
    if not transaction:
        print("No Transactions Yet.\n")
    else:
        print("-----Transactons History-----")
        for t in transaction:
            print('-',t)
        Deposit = sum (1 for t in transaction if 'Deposited' in t)
        Withdraw = sum(1 for t in transaction if 'Withdrawn' in t)
        print(f'\n Total ')
        print(f'\n Total Deposits: {Deposit}')
        print(f'\n Total Withdraws: {Withdraw}')
        
    
def menu():
    while True:
        print("====PyBank====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. CheckBalance")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice (1 - 5) : ")
        
        if choice == '1':
            amount = float(input("Enter your amount to deposit : "))
            Deposit(amount)
        elif choice == '2':
            amount = float(input("Enter your amount to Withdraw :"))
            Withdraw(amount)
        elif choice == '3':
            CheckBalance()
        elif choice == '4':
            View_Transaction_History()
        elif choice == '5':
            print("Exiting from Bank>> GOOD BYE!")
            break
        else:
            print("Invaild Input Try again")
menu()       