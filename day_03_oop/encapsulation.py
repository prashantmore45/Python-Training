class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance


account = Account(10000)
print(account.get_balance())  # Accessing the private attribute through a public method