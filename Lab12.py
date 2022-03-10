# Week 7 Lab 12
import string

# Q1
my_set = set('bcd')
your_set = set('abcde')


# print(my_set.issubset(your_set))  # A true
# print(your_set.issubset(my_set))  # B false

# Q2
# def check_heterogram(s):
#
#
# string1 = 'the big dwarf only jumps'
# string2 = 'given string is Heterogram'


# Q2
def check_pangram(s):
    char_set = {char.lower() for char in s if char not in string.punctuation and char != ' '}
    if len(char_set) == 26:
        return True
    else:
        return False


test = 'The quick brown fox jumps over the lazy dog'
# print(check_pangram(test))

# Q4
a_set = {"the", "coat", "had", "many", "colors", "red", "blue", "yellow"}
b_set = {"my", "coat", "had", "two", "main", "colors", "red", "blue"}

# A
x = a_set.intersection(b_set)  # coat had colors red blue
y = b_set.intersection(a_set)  # coat had colors red blue
# print(x)
# print(y)

# B
w = a_set.union(b_set)  # all of them combined
v = b_set.union(a_set)  # all of them combined
# print(w)
# print(v)

# C
t = a_set.difference(b_set)  # the many yellow
u = b_set.difference(a_set)  # my two main
# print(t)
# print(u)

# D
r = a_set.symmetric_difference(b_set)  # the many yellow my two main
s = b_set.symmetric_difference(a_set)  # the same


# print(r)
# print(s)

# Q5
def name(firstname, lastname):
    l_firstname = [char for char in firstname]
    l_lastname = [char for char in lastname]
    l_common = []
    for char in l_firstname:
        for ch in l_lastname:
            if char == ch and char not in l_common:
                l_common.append(char)
    print(l_firstname, l_lastname, l_common)


# name('fenna', 'kadir')

# Q6
def main():
    f = open('movie_list.txt', 'r')
    movie_dict = {}
    for line in f:
        create_movie_dict(line, movie_dict)


# def create_movie_database(movie_list):
#    movie_dict = {}


def create_movie_dict(line, movie_dict):
    print(line)
    rl = line.strip().split(',')
    a = rl[0]   # a is actor name
    # looping through movies and adding them to dictionary
    for x in range(1, len(rl)):
        l = rl[x].split('(')
        l[1] = l[1].replace(')', '', 1)
        m = (l[0], l[1])
        movie_dict[m] = []      # assign key to be movie name
        movie_dict[m].append(a)     # PROBLEM only one actor gets appended !!!
        # if m in movie_dict:
        #     movie_dict[m].append(a)
        # else:
        #     movie_dict[m] = a
    print(movie_dict)


main()
