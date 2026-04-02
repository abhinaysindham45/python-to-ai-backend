class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, owner, opening_balance):
        self.owner = owner
        self.__balance = opening_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.owner}] — Balance: ₹{self.__balance}"


# Creating accounts
acc1 = BankAccount("Alex", 10000)
acc2 = BankAccount("Sam", 20000)

# Transactions
acc1.deposit(5000)
acc1.withdraw(3000)

acc2.deposit(2000)
acc2.withdraw(25000)

# Print accounts
print(acc1)
print(acc2)