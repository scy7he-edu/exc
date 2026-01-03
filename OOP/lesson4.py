# приватные и защищенные атрибуты. Публичные интерфейсы
class BankAccount():
    
    def __init__(self):
        self.__balance = 0
        self._holder = 'Name'
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
acc = BankAccount() 
acc.deposit(500)
print(f'Текущий баланс: {acc.get_balance()}')