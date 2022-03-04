# week 5 Lab Test 1

# Question 1

def sum_divisors(number):
    # to avoid negative numbers
    if number < 0:
        print("Negative number. Only positive numbers accepted")
        return
    list_div = []
    sum_div = 0
    for x in range(1, number + 1):
        if number % x == 0:
            list_div.append(str(x))
            sum_div += x
    list_div = " + ".join(list_div)
    print(list_div, " = ", sum_div)


sum_divisors(20)
sum_divisors(33)
sum_divisors(50)
sum_divisors(-4)


# Question 2

def text_reverse(sentence):
    words_list = sentence.split()
    for x in range(0, len(words_list)):
        # to reverse every second word
        if x % 2 != 0:
            words_list[x] = words_list[x][::-1]
    new_sentence = " ".join(words_list)
    return new_sentence


input_str = input("Please enter your text here: ")
print(text_reverse(input_str))
