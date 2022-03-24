# Week 9 Lab 14

# Q1

class MyClass(object):
    def method1(self, param_list):
        self.local_list = []
        for element in param_list:
            if element > 10:
                self.local_list.append(element)

    def method2(self):
        self.sum_int = 0
        for element in self.local_list:
            self.sum_int += element
        return self.sum_int


inst1 = MyClass()
inst2 = MyClass()
inst1.method1([1, 2, 3])
# print(inst1.local_list)  # Line 1
inst1.method1([10, 11, 12])


# print(inst1.local_list)  # Line 2
# print(inst1.method2())  # Line 3
# inst2.method2() # Line 4

# A: empty list
# B: [11, 12]
# C: 23
# D: error because inst2.local_list atribute not instantiated

# Q2

class NewClass(object):
    def __init__(self, param_int=1):
        self.the_int = param_int
        if param_int % 2 == 0:
            self.parity = 'even'
        else:
            self.parity = 'odd'

    def process(self, instance):
        sum_int = self.the_int + instance.the_int
        if sum_int < 0:
            return 'negative'
        elif sum_int % 2 == 0:
            return 'even'
        else:
            return 'odd'

    def __str__(self):
        return 'Value {} is {}'.format(self.the_int, self.parity)


inst1 = NewClass(4)
inst2 = NewClass(-5)
inst3 = NewClass()


# print(inst1)  # Line 1
# print(inst1.parity)  # Line 2
# print(inst1.process(inst2))  # Line 3
# print(inst3.process(inst1))  # Line 4


# A: Value 4 is even
# B: Even
# C: Negative
# D: Odd

# 3A

class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def rectangle_perimeter(self):
        res = (self.height * 2) + (self.width * 2)
        return res

    def rectangle_area(self):
        result = self.width * self.height
        return result

    def __str__(self):
        return 'This rectangle is {} by {}'.format(self.width, self.height)


# main
r1 = Rectangle(5, 4)


# print(r1.height)
# print(r1.rectangle_area())


# 3B
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


# main
b1 = BankAccount('F Kadir', 'NL12INGB1234123456', '123456')
# print(b1)
# print(b1.deposit(100))
# print(b1.withdraw(50))
