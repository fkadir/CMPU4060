# Week 4 Lab 8
the_int_list = list(range(1, 7))  # * 3
the_int2_list = list(range(6, 11))
the_intt_list = [33, 11, 50]
the_str_list = "Always look on the bright side of life".split()

# # Q1
# def sum_list(the_list):
#     sum = 0
#     for x in the_list:
#         sum += x
#     return sum
#
#
# print(sum_list(the_int_list))
#
# # Q2
# def max_value(the_list):
#     max = 0
#     for x in the_list:
#         if x > max:
#             max = x
#     return max
#
#
# print(max_value(the_int_list))
#
#
# # Q3+4
# def word_with(the_list, word):
#     count = 0
#     for s in the_list:
#         if s[0] == word:
#             count += 1
#     return count
#
#
# print(word_with(the_str_list, "l"))
#
#
# # Q5
# def take_even(the_list):
#     even_list = []
#     for s in the_list:
#         if s % 2 == 0:
#             even_list.append(s)
#     return even_list
#
#
# print(take_even(the_int_list))
#
# Q6
# List = list(range(0, 100))
#
# # Q7
# def remove_duplicates(the_list):
#     the_list.sort()
#     for x in the_list:
#         next_one = the_list.index(x)+1
#         while x == the_list[next_one]:
#             the_list.remove(x)
#             if len(the_list) == next_one:
#                 break
#     return the_list
#
#
# print(remove_duplicates(the_int_list))
#
# # Q8
# def in_common(the_list, the_list2):
#     for x in the_list:
#         for y in the_list2:
#             if x == y:
#                 return True
#     return False
#
#
# print(in_common(the_int_list, the_int2_list))
#
# # Q9
# def not_in_common(the_list, the_list2):
#     difference = []
#     for x in the_list:
#         if x in the_list2:
#             continue
#         else:
#             difference.append(x)
#     return difference
#
#
# print(not_in_common(the_int2_list, the_int_list))
#
# # Q10
# strint = [str(i) for i in the_intt_list]
# merge = int("".join(strint))
# print(merge)
#
# # Q11
# def weird_sum(the_list):
#     sum_list = []
#     for x in the_list:
#         i = the_list.index(x)
#         if i == 0:
#             sum_list.append(x + the_list[i+1])
#         elif i == len(the_list)-1:
#             sum_list.append(the_list[i-1] + x)
#         else:
#             sum_list.append(the_list[i-1] + x + the_list[i+1])
#     return sum_list
#
#
# print(weird_sum(the_int_list))
