# Week 10 L14.2 Examples

# ex 1
import math


class Point(object):
    def __init__(self, x_param=0.0, y_param=0.0):
        self.x = x_param
        self.y = y_param

    def distance(self, param_pt):
        x_diff = self.x - param_pt.x  # x1 - x2
        y_diff = self.y - param_pt.y  # y1 - y2
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def sum(self, param_pt):
        # new_pt = Point()
        # new_pt.x = self.x + param_pt.x
        # new_pt.y = self.y + param_pt.y
        # return new_pt
        return Point(self.x + param_pt.x, self.y + param_pt.y)

    def __str__(self):
        return "{:.2f}, {:.2f}".format(self.x, self.y)


# ex 2
class Sentence(object):
    def __init__(self, s=''):
        self.sentence_string = s

    def get_first_word(self):
        words = self.sentence_string.split()
        return words[0]

    def get_all_words(self):
        return self.sentence_string.split()

    def replace(self, index, new_word):
        words = self.sentence_string.split()
        if 0 <= index < len(words):
            words[index] = new_word
            self.sentence_string = ' '.join(words)
        else:
            print("Error in replace: index out of range.")

    def __str__(self):
        return self.sentence_string

# my_sentence = Sentence("I'm going back")
# my_sentence.replace(2, "home")
# print(my_sentence)
