class Account:
    
    def __init__(self, number, password, balance): #A new bank account should be defined with a given account number, password and balance
        self.__accountNumber = number
        self.__accountPassword = password
        self.__accountBalance = balance

    def getNumber(self): 
        #This method should return the account number of this account
        return self.__accountNumber
    
    def checkPassword(self, password): 
       #This method should check if a given password is equal to the password for this account
       if password == self.__accountPassword:
           return 1
       else:
           return -1

    def getBalance(self): 
        #This method should return the account number of this account
        return self.__accountBalance

    def setBalance(self, newBalance):
        #This method should change the balance of this account to a specified new value
        self.__accountBalance = newBalance
        print(f'The balance for this account has been updated to {newBalance}')

class Bank:
    def __init__(self): #A new bank is defined with a list of bank accounts and a value that keeps track of the account number of the most recently added account
        self.__accounts = []
        self.__latestAccount = -1 
            
    def login(self):
        #This method should ask the user to give their account number and password, returning the account number if they match, or returning -1 if not
        #1. Get valid user input
        while True:
        #use a while look to make sure the program does not proceed without valid info
            try:
                accNum = int(input('Enter the account number: '))
                accPass = input('Enter the account password: ')
                break 
            except ValueError:
                print('A whole number is required for the account number')
        #2. Iterate over accounts in the list to check if given account number is in the list of registered accounts
        for account in self.__accounts:
            if account.getNumber() == accNum and account.checkPassword(accPass):
                return account.getNumber()
        return -1
    def deposit(self, number):
        #This method should ask the user how much money they want to deposit into their account, and correctly update the balance of their account
        while True:
            try:
                depositAmount = float(input('Enter the amount to be deposited: '))
                break
            except ValueError:
                print('Amount to be deposited must be numeric')
        #access the account to be updated
        #retrieve the current balance
        #update the current balance
        #set the balance
        newBalance = self.__accounts[number].getBalance() + depositAmount
        self.__accounts[number].setBalance(newBalance)
    def withdraw(self, number):
        #This method should ask the user how much money they want to withdraw from their account, and correctly update the balance of their account
        #1. Validate an amount to withdraw
        while True:
            try:
                withdrawAmount = float(input("Enter the amount you would like to withdraw: "))
                break
            except ValueError:
                print('Please enter a numeric amount')
        '''
        2.
        - Access the account from which to withdraw
        - check if the balance is more than the withdraw amount
        - retrieve the current balance
        - deduct and update balance
        '''  
        if self.__accounts[number].getBalance() >= withdrawAmount:
            newBalance = self.__accounts[number].getBalance() - withdrawAmount
            self.__accounts[number].setBalance(newBalance)
        else:
            print('You have insufficient funds to make that withdrawal') 
    def checkBalance(self, number):
        #This method should display a message telling the user how much money is in their account
        print(f'Your account balance is £{self.__accounts[number].getBalance():.3f}')
    def addAccount(self):
        #This method should create a new account with an account number 1 larger than the account number or the last account created, a password given by the user, and a balance of 0. The account should be added to the bank's list of accounts
        self.__latestAccount += 1
        print('A new account will be created for you')
        input('Press any key to continue')
        accountPassword = input('Enter the password to this new account: ')
        #create a new account object with a default balance of 0
        newAccount = Account(self.__latestAccount, accountPassword, 0)
        print(f'A new account with the account number {newAccount.getNumber()} has been created')
        
        #add the new account to the accounts list
        self.__accounts.append(newAccount)
def main():
    bank = Bank()
    loggedIn = False
    quitting = False
    
    while not loggedIn and not quitting:
        response = input("Do you have an account? (y/n/quit)")
        if response == "y":
            account = bank.login()
            if account != -1:
                loggedIn = True
        elif response =="n":
            bank.addAccount()
        elif response =="quit":
            quitting = True
            
    while not quitting:
        option = input("Press 1 to check your balance\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to exit:\n")
        if option == "1":
            bank.checkBalance(account)
        elif option == "2": 
            bank.deposit(account)
            bank.checkBalance(account)
        elif option == "3":
            bank.withdraw(account)
            bank.checkBalance(account)
        elif option == "4":
            quitting = True
        else:
            print("Invalid option selected")
    
if __name__ == '__main__':
    main()