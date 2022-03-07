# CODEWARS

# digital root
# best practice
def digital_root(n):
    print(n)
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# my solution
def my_digital_root(n):
    n = str(n)
    if len(n) < 2:
        return int(n)
    while len(n) >= 2:
        sumy = 0
        for x in n:
            sumy += int(x)
        n = str(sumy)
    return sumy


# find outliers
# best practice
def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


# my solution
def my_find_outlier(integers):
    odd, even = [], []
    for x in range(0, len(integers)):
        if integers[x] % 2 == 0:
            even.append(integers[x])
        else:
            odd.append(integers[x])

    if len(even) < len(odd):
        return even[0]
    else:
        return odd[0]


# create strings of 2 characters from string
# best practice
import re


def solution(s):
    return re.findall(".{2}", s + "_")


def solution1(s):
    result = []
    if len(s) % 2:
        s += '_'
        print(s)
    for i in range(0, len(s), 2):
        result.append(s[i:i + 2])
    return result


# my solution
def my_solution(s):
    if len(s) % 2 != 0:
        s = list(s)
        s.append("_")
        s = "".join(s)
    l = [s[x:x + 2] for x in range(0, len(s), 2)]  # step 2 in range instead if x % 2 == 0
    return l


print(solution1("abcdefghijk"))


# insert space in string before uppercase letter
# Best Practice
def insert_space(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


def insert_space2(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string


print(insert_space("breakCamelCase"))
print(insert_space2("breakCamelCase"))
