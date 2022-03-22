# Week 9 Lab 13

# Q1. parameters are the variables that we can define in the function declaration and arguments
# are the variables given to the function for execution

# Q2 [100, 6, 7]
import copy


def my_function(b_list):
    b_list[0] = 100
    a_list = [1, 2, 3]


a_list = [5, 6, 7]


# my_function(a_list)
# print(a_list)

# Q3 name is not defined
def f(a, b=2):
    pass


# f(a=3, b=4)
# print(a, b)

# Q4
# v1
def add_one(number):
    x = 1
    number = number + x
    print(number, x)


# add_one(3)


# v2
def add_one(number):
    x = 1
    number = number + x
    print(number)
    return x


# x = add_one(3)
# print(x)

# Q5
def func1(list1, list2, str1):
    if len(list1) > 3:
        list1 = list1[:3]
    list2[0] = 'goodbye'
    str1 = ''.join(list2)


arg1_list = ['a', 'b', 'c', 'd']
arg2_list = ['hello', 'mother', 'and', 'father']
arg_str = 'sister'

func1(arg1_list, arg2_list, arg_str)


# print(arg1_list)  # A   ['a', 'b', 'c', 'd']
# print(arg2_list)  # B   ['goodbye', 'mother', 'and', 'father']
# print(arg_str)  # C     sister


# Q6 A
def remove_even(list1):
    list1 = [x for x in list1 if x % 2 != 0]
    return list1


# B
def remove_odd(list2):
    list2 = [y for y in list2 if y % 2 == 0]
    return list2


# C
def remove(list3, b):
    if b is True:
        list3 = [z for z in list3 if z % 2 == 0]
    else:
        list3 = [z for z in list3 if z % 2 != 0]
    return list3


x_list = [n for n in range(0, 20)]


# x_list = remove_odd(x_list)
# x_list = remove_even(x_list)
# x_list = remove(x_list, True)
# print(x_list)

# Q7 A
def palindrome(str1):
    str1 = str1.lower()
    list1, list1_reverse = list(str1), list(str1)
    list1_reverse.reverse()
    while ' ' in list1:
        list1.remove(' ')
    while ' ' in list1_reverse:
        list1_reverse.remove(' ')
    if list1 == list1_reverse:
        return True
    else:
        return False


def display_palindrome():
    string1 = input("Please input your string here: ")
    result = palindrome(string1)
    if result is True:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome :(")


# display_palindrome()

# Q8
def is_it_sorted(list1):
    list2 = copy.deepcopy(list1)
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


# print(is_it_sorted([9, 8, 6, 5, 3, 2, 10, 23, 45]))
