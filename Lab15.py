# Week 11 Lab 15
# Q1

class Vehicle(object):

    def __init__(self, model_year=0000, total_mileage=0, VIN=0, engine='NA'):
        self.model_year = model_year
        self.total_mileage = total_mileage
        self.VIN = VIN
        self.engine = engine

    def __str__(self):
        return "This vehicle with VIN number {} was made in {}, has a total mileage of {} and has a {} engine" \
            .format(self.VIN, self.model_year, self.total_mileage, self.engine)


class Car(Vehicle):
    def __init__(self, model_year=0000, total_mileage=0, VIN=0, engine='NA'):
        Vehicle.__init__(self, model_year, total_mileage, VIN, engine)

    def __str__(self):
        return "This car with VIN number {} was made in {}, has a total mileage of {} and has a {} engine" \
            .format(self.VIN, self.model_year, self.total_mileage, self.engine)


class Truck(Vehicle):
    def __init__(self, model_year=0000, total_mileage=0, VIN=0, engine='NA'):
        Vehicle.__init__(self, model_year, total_mileage, VIN, engine)

    def __str__(self):
        return "This truck with VIN number {} was made in {}, has a total mileage of {} and has a {} engine" \
            .format(self.VIN, self.model_year, self.total_mileage, self.engine)


class SUV(Vehicle):
    def __init__(self, model_year=0000, total_mileage=0, VIN=0, engine='NA'):
        Vehicle.__init__(self, model_year, total_mileage, VIN, engine)

    def __str__(self):
        return "This SUV with VIN number {} was made in {}, has a total mileage of {} and has a {} engine" \
            .format(self.VIN, self.model_year, self.total_mileage, self.engine)


class Minivan(Vehicle):
    def __init__(self, model_year=0000, total_mileage=0, VIN=0, engine='NA'):
        Vehicle.__init__(self, model_year, total_mileage, VIN, engine)

    def __str__(self):
        return "This minivan with VIN number {} was made in {}, has a total mileage of {} and has a {} engine" \
            .format(self.VIN, self.model_year, self.total_mileage, self.engine)


car = Car(2000, 3000, 123456, '5XNM6')


# print(car)


# Q2
class BankAccount(object):
    def __init__(self, name, iban, account_number, funds=0, last_transactions=[]):
        self.name = name
        self.iban = iban
        self.account_number = account_number
        self.funds = funds
        self.last_transactions = last_transactions

    def __str__(self):
        return 'Account {} with {} belongs to {}'.format(self.account_number, self.iban, self.name)

    def withdraw(self, withdraw_amount):
        self.funds -= withdraw_amount
        return 'current available funds: {}'.format(self.funds)

    def deposit(self, deposit_amount):
        self.funds += deposit_amount
        return 'current available funds: {}'.format(self.funds)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, name, iban, account_number, min_balance=0, funds=0, last_transactions=[]):
        BankAccount.__init__(self, name, iban, account_number, funds, last_transactions)
        self.min_balance = min_balance

    def withdraw(self, withdraw_amount):
        check = self.funds - withdraw_amount
        if check >= self.min_balance:
            self.funds = check
            return 'current available funds: {}'.format(self.funds)
        else:
            return 'not enough funds'


b2 = MinimumBalanceAccount('F Kadir', 'NL12INGB1234123456', '123456', 10)
# b2.deposit(100)
# print(b2.withdraw(50))
