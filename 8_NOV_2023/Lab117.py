class BankAccount:
    def __init__(self):
        self.balance = 0 # Instance Variable ( You can access it via only Object)
        self.__private_var = 100

    def deposit(self, amount):  # Public Function
        # self.balance = self.balance + amount
        self.balance += amount

    def _withdraw(self, amount):  # Protected
        self.balance -= amount

    def __show_balance(self):
        print("Your Bal", self.balance)

    def IS_Auth_True_show_bal(self, isAuth):
        if isAuth:
            self.__show_balance()
        else:
            print("You are not Auth")

    def do_withdraw_by_bank_manager(self,amount):
        self._withdraw(amount=amount)


jp_chase = BankAccount()
jp_chase.deposit(1000)
jp_chase._withdraw(499)  # Not a Good practice ( Protected)
# jp_chase.__show_balance()

# Never use this
jp_chase._BankAccount__private_var = 100
print(jp_chase._BankAccount__private_var) # Super Bad Pratice - Python allow this , Java

# Write the code to Auth - Dev
# jp_chase.IS_Auth_True_show_bal(True)
jp_chase.IS_Auth_True_show_bal(False)
