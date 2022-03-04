# Week 6 Lab 9
import copy

# Q1
str_list = ['hi', 'mom', 'dad', ['grandma', 'grandpa']]
new_list = str_list
copy_list = str_list[:]

str_list[0] = 'bye'
new_list[1] = 'mother'
copy_list[2] = 'father'
copy_list[-1][0] = 'nanna'

print(str_list)  # Line 1
print(new_list)  # Line 2
print(copy_list)  # Line 3

# A ['bye', 'mother', 'dad', ['nanna', 'grandpa']]
# B ['bye', 'mother', 'dad', ['nanna', 'grandpa']]
# C ['hi', 'mom', 'father', ['nanna', 'grandpa']]

# Q2
ListA = [1, 2, 3, 4, 5]
ListB = ListA
ListA[2] = 10
print(ListB[2])
# 10

# Q3
list1 = [1, 2, 99]
list2 = list1
# list3 = list2
list3 = copy.deepcopy(list2)
list1 = list1.remove(1)

print(list3)

# A [2, 99]
# B list3 = copy.deepcopy(list2)

# Q4
L = [1,2,3,4]
S = ''.join([str(i) for i in L])
print(S)

# Q5
def add_fractions(frac1, frac2):
    result = (frac1[0] / frac1[1]) + (frac2[0] / frac2[1])
    return result


def multiply_frac(frac1, frac2):
    result = (frac1[0] / frac1[1]) * (frac2[0] / frac2[1])
    return result


tuple1 = (2, 4)
tuple2 = (3, 4)

print(add_fractions(tuple1, tuple2))
print(multiply_frac(tuple1, tuple2))


# Q6
def sort_tuple(List):
    List.sort(key=lambda x: x[1])
    return List


L = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ('item4', '22.3'), ('item5', '13.8')]
print(sort_tuple(L))

# Q7
a = [n ** 2 for n in range(1, 11)]
b = [n.upper() for n in ['Red', 'Blue', 'Green', 'Black', 'White']]
c = [n for n in range(1, 1001) if n % 7 == 0]
d = [n for n in range(1, 1001) if '3' in str(n)]
e = [s for s in 'how many can i fit in hure' if s not in ['e', 'o', 'i', 'u', 'a']]
e = "".join(e)
sentence = 'hello how are you are you sure though'
f = [w for w in sentence.split() if len(w) < 4]
g = [number for number in range(1, 1001) if True in [True for n in range(2, 10) if number % n == 0]]
