# week 4 Lab 7 Functions
import random

Int_input = int(input("Input your int here: "))
# Int_input2 = int(input("Input your int here: "))
# Str_input = input("Input your word here pls: ")


# # Q1
# def Print_Numbers(num):
#     for x in range(1, num + 1):
#         print(x)
#     pass
#
#
# Print_Numbers(Int_input)
#
#
# # Q2
# def OddorEven(num):
#     for x in range(0, num + 1):
#         if x % 2 == 0:
#             print(x, " is even")
#         else:
#             print(x, " is odd")
#     pass
#
#
# OddorEven(Int_input)
#
#
# # Q3
# def Multiply9(num):
#     for x in range(0, num + 1):
#         res = x * 9
#         print(x, "* 9 =", res)
#     pass
#
#
# Multiply9(Int_input)
#
#
# # Q4
# def Summation(num):
#     sump = 0
#     for x in range(1, num + 1):
#         sump += num
#
#     print(sump)
#     pass
#
#
# Summation(Int_input)
#
#
# # Q5
# def factorial(num):
#     sump = 1
#     for x in range(2, num + 1):
#         sump = sump * x
#     print(sump)
#     pass
#
#
# factorial(Int_input)
#
#
# # Q6
# def slice_baby(word):
#     theEnd = len(word) - 1
#     if len(word) < 4:
#         print("word is too small, too bad")
#         exit
#     else:
#         new_word = word[0] + word[1] + word[theEnd - 1] + word[theEnd]
#         print(new_word)
#     pass
#
#
# slice_baby(Str_input)
#
#
# # Q7
# def remove_odd(word):
#     new_word = word[::2]
#     return new_word
#
#
# print(remove_odd(Str_input))
#
#
# # Q8
# def half_string(word):
#     half = len(word) // 2
#     new_word = word[:half]
#     return new_word
#
#
# print(half_string(Str_input))
#
#
# # Q9
# def insert_string_middle(word, middle):
#     half = len(word) // 2
#     new_word = word[:half] + middle + word[half:]
#     return new_word
#
#
# print(insert_string_middle("[[[]]]", Str_input))
#
#
# # Q10
# def remove_part_string(word, ind1, ind2):
#     new_word = word[:ind1] + word[ind2 + 1:]
#     return new_word
#
#
# print(remove_part_string(Str_input, Int_input, Int_input2))


# # Q11
# def simple_player(si_amount_beans):
#     amount_taken = random.randint(1, 3)
#     new_amount_beans = si_amount_beans - amount_taken
#     print(amount_taken)
#     return new_amount_beans
#
#
# def smart_player(sm_amount_beans):
#     amount_taken = int(input("how many do you wanna take: "))
#     new_amount_beans = sm_amount_beans - amount_taken
#     print(amount_taken)
#     return new_amount_beans
#
#
# amount_beans = 16
# count = 0
# while amount_beans > 0:
#     if count % 2 == 0:
#         amount_beans = simple_player(amount_beans)
#         if amount_beans < 0:
#             print("simple player loses!")
#     else:
#         amount_beans = smart_player(amount_beans)
#         if amount_beans < 0:
#             print("smart player loses!")
#     count += 1
