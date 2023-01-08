class BankAccount:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount()    
account2 = BankAccount()

account1.set_details("Tyler")
account2.set_details("Joseph")

account1.deposit(25)
account2.deposit(15)

account1.withdraw(5)
account2.withdraw(3)

account1.display()
account2.display()