# Week 3 Lab 5

#Q1
input_string = input("Input your string here: ")

for char in input_string:
    print(char, end="")

#Q2
count = 0
for char in input_string:
    count += 1

print(count)

#Q3
given_string = "Monty Python"

print(given_string[0])
print(given_string[-1])
print(given_string[len(given_string)-1])
print(given_string[:5])

#Q3 (again)

if len(input_string) >= 4:
    print(input_string[:2]+input_string[-2:])
else:
    print("String is too small, please input a string of min length 4")

#Q4
given_string = "Monty"
middle_index = int(len(given_string)/2)

print(given_string[middle_index])
print(given_string[:middle_index])
print(given_string[middle_index+1:])

# Q5
# A Turns s1 or s2 into s4
# B turns the lowercase letters into uppercase and other way around
# C turns all letters in upper case
# D turns all letters into lower case
# E capitalizes every word in a sentence

#Q6
for x in range(1, len(input_string)+1):
    print(input_string[-x], end="")

# Q7
for x in range(len(input_string)):
    new_value = ord(input_string[x])+1
    encrypt = chr(new_value)
    print(encrypt, end="")

# Q7 Part 1
input_integer = int(input("put your integer input here: "))
if input_integer == 0:
    print("It is 0")
elif input_integer < 0:
    print("It is negative")
else:
    remain = [None] * 50
    count = 0
    while input_integer > 0:
        rem_input_integer = input_integer
        input_integer = input_integer//2
        remain[count] = rem_input_integer%2
        count += 1

    x = count
    while x > 0:
        x -= 1
        print(remain[x], end="")

# Q7 Part 2
input_binary = input("input your binary number here: ")
index = len(input_binary)
count = 0
number = 0
while index > 0:
    index -= 1
    i = int(input_binary[index])
    number += (2**count)*i
    count += 1
print(number)


