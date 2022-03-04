# import string
#
# input_str = input("Please insert your string here: ")
# input_int = int(input("Enter inclusive top limit: "))
#
# # Q1
# for i in input_str:
#     index = input_str.index(i)
#     int_value = ord(i) + index
#     encrypt = chr(int_value)
#     print(encrypt, end="")
#
#
# # Q2
# def reformat_time(dt):
#     date, time = dt.split()
#     day, month, year = map(int, date.split("/"))
#     h, m, s = map(int, time.split(":"))
#     if day < 1 or day > 31:
#         print("error day")
#         return
#     elif month < 1 or month > 12:
#         print("error month")
#         return
#     elif h < 0 or h > 23:
#         print("error hour")
#         return
#     elif m < 0 or m > 59:
#         print("error minute")
#         return
#     elif s < 0 or s > 59:
#         print("error second")
#         return
#     else:
#         print(date)
#         print(time)
#         print(str(month) + "/" + str(year))
#         if h > 11:
#             print("PM")
#         else:
#             print("AM")
#
#
# reformat_time(input_str)
#
#
# # Q3
# def kaprekar_check(number):
#     value = str(number ** 2)
#     for x in range(1, len(value)):
#         v1 = int(value[:x])
#         v2 = int(value[x:])
#         if v1 + v2 == number:
#             return True
#     return False
#
#
# def print_kaprekar_numbers(limit):
#     for x in range(10, limit + 1):
#         if kaprekar_check(x):
#             print(x, end=" ")
#     return
#
#
# print_kaprekar_numbers(input_int)
#
#
# def replace_all(sentence, toBeReplaced, replacedWith):
#     if sentence[-1] == "." or sentence[-1] == "?" or sentence[-1] == "!":
#         sentence = sentence[:-1]
#     sentence = sentence.split()
#     new = sentence
#     for x in range(0, len(sentence)):
#         for y in range(0, len(toBeReplaced)):
#             if sentence[x] == toBeReplaced[y]:
#                 new[x] = replacedWith[y]
#     new = " ".join(new)
#     return new
#
#
# print(replace_all("John and Bill went to the shop", ["John", "Bill", "Shop"], ["Mary", "Ann", "Cinema"]))

