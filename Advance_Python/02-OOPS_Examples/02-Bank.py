class Bank:

    def __init__(self,name,acc_balance):
        self.name = name
        self.acc_bal = acc_balance

    def authentication(self):
        user_pin = int(input("Enter your PIN : "))

        if user_pin == 1234:
            self.menu()
        else:
            print("You are fraud....")

    def menu(self):
        print("""
        1. Withdraw
        2. Deposit
        3. Quit
        """)

        user_option = {
            "1" : self.withdraw,
            "2" : self.deposit,
            "3" : quit
        }

        user_choice = input("Enter your choice : ")
        print("Remaining Balance : ",user_option.get(user_choice)())

    def withdraw(self):
        withdraw_amount = int(input("Enter amount to withdraw : "))
        self.acc_bal = self.acc_bal - withdraw_amount
        return self.acc_bal

    def deposit(self):
        deposit_amount = int(input("Enter amount to withdraw : "))
        self.acc_bal = self.acc_bal + deposit_amount
        return self.acc_bal


    def loan_avail(self):

        if self.acc_bal > 20000:
            print("Loan available")
        else:
            print("Try Next Year....")


obj_1 = Bank("Ram",25000)
obj_1.authentication()
obj_1.loan_avail()
