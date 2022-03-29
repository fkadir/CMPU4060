# Week 10 Lab 15
import math


# Q1
class TestClass(object):

    def __init__(self, param_str=''):
        self.the_str = ''
        for c in param_str:
            if c.isalpha():
                self.the_str += c

    def __add__(self, param):
        if type(param) == TestClass:
            the_str = self.the_str + param.the_str
            return TestClass(the_str)
        else:
            return self

    def __str__(self):
        return 'Value: {}'.format(self.the_str)


inst1 = TestClass('abc')
inst2 = TestClass('123ijk')
sumInst1 = inst1 + inst2
sumInst2 = inst1 + 'xyz'


# print(inst1)  # Line 1                              A Value: abc
# print(sumInst1)  # Line 2                           B Value: abcijk
# print(sumInst2)  # Line 3                           C Value: abc
# print(isinstance(sumInst2, TestClass))  # Line 4    D True

# Q2
class WholeNumber(object):

    def __init__(self, num):
        if num >= 0 and type(num) == int:
            self.number = num
        else:
            raise 'Invalid input: a Whole Number cannot be negative or a float'

    def __add__(self, other):
        if type(other) == WholeNumber:
            n = self.number + other.number
            return WholeNumber(n)
        else:
            return 'Invalid input'

    def __sub__(self, other):
        if type(other) == WholeNumber:
            s = self.number - other.number
            if s > 0:
                return WholeNumber(s)
            else:
                return 'Invalid result'
        else:
            return 'Invalid input'

    def __mul__(self, other):
        if type(other) == WholeNumber:
            p = self.number * other.number
            return WholeNumber(p)
        else:
            return 'Invalid input'

    def __str__(self):
        return 'Value: {}'.format(self.number)


n1 = WholeNumber(2)
n2 = WholeNumber(3)
add = n1 + n2
add1 = n2 + 7
sub = n1 - n2
sub1 = n2 - n1
mul = n1 * n2
mul1 = n1 * 5


# print(n1)
# print(add)
# print(add1)
# print(sub)
# print(sub1)
# print(mul)
# print(mul1)

# Q3
class LinearEquation(object):

    def __init__(self, m, b):
        self.m = m
        self.b = b

    def __add__(self, equation):
        if type(equation) == LinearEquation:
            sum_m = self.m + equation.m
            sum_b = self.b + equation.b
            return LinearEquation(sum_m, sum_b)
        else:
            return 'Invalid Input'

    def value(self, x):
        y = (self.m * x) + self.b
        return y

    def compose(self, equation):
        if type(equation) == LinearEquation:
            self.m = self.m * equation.m
            self.b = self.m * equation.b + self.b
        else:
            return 'Invalid Input'

    def __repr__(self):
        return 'LinearEquation({}, {})'.format(self.m, self.b)

    def __str__(self):
        return 'y = {}x + {}'.format(self.m, self.b)


e1 = LinearEquation(2, 5)
e2 = LinearEquation(3, 7)
s1 = e1 + e2


# print(e1.value(1))
# print(e2)
# print(repr(e2))
# print(s1)
# e2.compose(e1)
# print(e2)


# Q4
class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        if type(v) == Vector:
            return Vector(self.x + v.x, self.y + v.y)
        else:
            return 'Invalid Input'

    def __mul__(self, v):
        if type(v) == int:
            return Vector(self.x * v, self.y * v)
        elif type(v) == Vector:
            return self.x * v.x + self.y * v.y
        else:
            return 'Invalid Input'

    def __sub__(self, v):
        if type(v) == Vector:
            return Vector(self.x - v.x, self.y - v.y)
        else:
            return 'Invalid Input'

    def magnitude(self):
        return math.sqrt(self.x + self.y)

    def __str__(self):
        return 'Vector: ({}, {})'.format(self.x, self.y)


v1 = Vector(3, 6)
v2 = Vector(-2, 0)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 4
v6 = v1 * v2
print(v3)
print(v4)
print(v5)
print(v6)
print(v1.magnitude())
