import random
# Week 3 Lab 6

#Q1 result is cat
s = "CAT"
s.upper().lower()

#Q2
input_string = input("input your string here: ")
print(input_string.lower())

#Q3
print(input_string.count("h"))

#Q4
print(input_string.strip("h"))

#Q5A
s = "#"
print(s+s+s+s+s+s) #80 times
print(s*80)
#B
s = "# \n"
print(s*30)

#Q6
string_2 = ""
input_string = input_string.lower()
for char in input_string:
    if char == "b":
        print(" ")
    else:
        string_2 += char

print(string_2)

#Q7 slide 11
print("Melting and Boiling Points of Alkanes")
print("{:<10} {:<30} {:<30}".format("Name", "Melting Point (deg C)", "Boiling Point (deg C)"))
print("{:<10} {:<30d} {:<30d}".format("Methane", -162, -183))
print("{:<10} {:<30d} {:<30d}".format("Ethane", -89, -172))
print("{:<10} {:<30d} {:<30d}".format("Propane", -42, -188))
print("{:<10} {:<30.1f} {:<30d}".format("Butane", -0.5, -135))

#Q8
length = len(input_string)-1
swap_1 = random.randint(0, length)
swap_2 = random.randint(0, length)
while swap_1 >= swap_2:
    swap_2 = random.randint(0, length)

new_string = input_string[0:swap_1] + input_string[swap_2] + input_string[swap_1+1:swap_2] + input_string[swap_1] + input_string[swap_2+1:length+1]
print(new_string)

#Q9
first = input_string[0]
length = len(input_string)
if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    new_string = input_string + "yay"
elif first == ".":
    quit()
else:
    new_string = input_string[1:length] + input_string[0]
    for char in new_string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            new_string += "ay"
            break
        else:
            new_string = new_string[1:length] + new_string[0]

print(new_string)