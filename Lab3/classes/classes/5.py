class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.dep = dep
        self.balance = self.balance + self.dep
        if self.balance < 0:
            return "Your balance is overdrawned"
        return f"Welcome, {self.owner} \nYour balance after deposit is: {self.balance}"
    def withdraw(self, wit):
        self.wit = wit
        self.balance = self.balance - self.wit
        if self.balance < 0:
            return "Your balance is overdrawned"
        return f"Welcome, {self.owner} \nYour balance after withdraw is: {self.balance}"
    def seebalance(self):
        if self.balance < 0:
            return "Your balance is overdrawned"
        return f"Welcome, {self.owner} \nYour balance is: {self.balance}"

    
acc = Account("Michael", 5000)
print(acc.seebalance())
print(acc.deposit(120))
print(acc.withdraw(500))
print(acc.withdraw(6000))
print(acc.deposit(1500))
