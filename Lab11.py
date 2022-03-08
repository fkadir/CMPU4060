# Week 7 Lab 11 Dictionaries

# Q1 A
import copy
import string
from webbrowser import open_new_tab

D = {'a': 2, 'x': 7, 'r': 5}
x = D['x']

print(x)


# B
def get_key(val, the_dict):
    result = "".join([key for key, value in the_dict.items() if val == value])
    return result


def get_key2(val, the_dict):
    for key, value in the_dict.items():
        if val == value:
            return key
    return 'value has not been found'


print(get_key(7, D))
print(get_key2(7, D))

# Q2
D = {'a': 15, 'c': 35, 'b': 55}
a = [keys for keys in D]  # a = D.keys()
b = [val for val in D.values()]  # b = D.values()
c = [(keys, val) for keys, val in D.items()]  # c = D.items()
d = sorted(D.items())
e = sorted(D.items(), key=lambda x: x[1])

print(a, b, c, d, e, sep="\n")


# Q3
def generate_dict(z):
    the_dict = {z: z * z for z in range(1, z + 1)}
    return the_dict


print(generate_dict(5))


# Q4
def combine_dict(d1, d2):
    d3 = copy.deepcopy(d1)
    # d3 = {d3[key] += val if key in d3.keys() else d3[key] = val for key, val in d2.items()}
    for key, val in d2.items():
        if key in d3.keys():
            d3[key] += val

        else:
            d3[key] = val
    return d3


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print(combine_dict(d1, d2))


# Q5
def int_to_words(x):
    word_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                 9: "nine"}
    x = list(str(x))
    result = [word_dict[int(char)] for char in x]
    return " ".join(result)


print(int_to_words(628098))


# Q6
def capital_dict():
    capitals_countries = {}
    while True:
        capital = input("input capital here: ")
        country = input("input country here: ")
        if capital == "exit":
            break
        else:
            capitals_countries[country] = capital
    print(sorted(capitals_countries.values()))


capital_dict()


# Q7
def main():
    word_count_dict = {}
    file = open("hare_and_tortoise.txt")
    for line in file:
        process_line(line, word_count_dict)

    write_to_html(word_count_dict)


def process_line(line, wc_dict):  # process the line to get lowercase words to add to the dictionary
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        word = word.lower().strip()
        word = word.strip(string.punctuation)  # get punctuation out
        add_word(word, wc_dict)


def add_word(word, wc_dict):  # create word frequency dictionary
    if word in wc_dict:
        wc_dict[word] += 1
    else:
        wc_dict[word] = 1


def write_to_html(d):  # function that creates word cloud in html
    # creates list of strings of span elements for every word in frequency dictionary excluding stopwords
    l = ["""<span style="font-size: """ + str(v * 10) + """px"> """ + str(k) + """ </span>""" for k, v in d.items() if
         not in_stop_words(k)]
    l = " ".join(l)
    # insert list of span elements into whole html file string
    whole = """<!DOCTYPE html> <html> <head lang="en"> <meta charset="UTF-8"> <title>Tag Cloud Generator</title> 
    </head> <body> <div style="text-align: center; width: 15%; vertical-align: middle; font-family: arial; color: 
    white; background-color:black; border:1px solid black"> {0} </div> </body>> </html>""".format(l)
    f = open("L11-7.html", 'w')
    f.write(whole)
    f.close()
    open_new_tab("L11-7.html")


def in_stop_words(word):  # check if input is present in stopwords.txt file and return boolean as appropriate
    with open("stopwords.txt", 'r') as f:
        contents = f.read()
        if word in contents:
            return True
        else:
            return False


main()
