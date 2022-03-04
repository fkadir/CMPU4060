# Week 6 Lab 10

# Q1
def print_fl():
    while True:
        try:
            number_float = float(input("Input a floating-point number: "))
        except ValueError:
            print("Provide a float value ...")
            continue
        else:
            break
    print("Number is", number_float)


# print_fl()


# Q2
def safe_input(prompt, param_type):
    while True:
        print(type(prompt))
        if param_type == int:
            try:
                print(param_type)
                prompt = int(prompt)
                print("success int")
                return prompt
            except ValueError:
                print("fail int")
        elif param_type == float:
            try:
                prompt = float(prompt)
                print("success float")
                return prompt
            except ValueError:
                print("fail float")
        elif param_type == str:
            try:
                prompt = str(prompt)
                print("success str")
                return prompt
            except ValueError:
                print("fail str")
        prompt = input("try input of type " + str(param_type))


# safe_input(1, float)

# Q3
def prompt_open(mode):
    while True:
        try:
            if mode in ['r', 'w']:
                input_f = input("Insert filename: ")
                read_f = open(input_f, mode)
                return input_f
            else:
                mode = input("Insert different mode: ")
        except IOError:
            print("try again")


# m = input("Insert mode here: ")
# print(prompt_open(m))


# Q4
# find the line in a file
def operations(num1, num2, num3):
    try:
        result = (num1 / num2) + num3
        return result
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


# print(operations(5, 0, 0))


# Q5
while True:
    try:
        file_str = input("Open what file: ")
        input_file = open(file_str)  # potential user error
        while True:
            try:
                find_line_str = input("Which line (integer): ")
                find_line_int = int(find_line_str)  # potential user error
                line_count_int = 1
                for line_str in input_file:
                    if line_count_int == find_line_int:
                        print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
                        input_file.close()
                        exit()
                    line_count_int += 1
                else:
                    # get here if line sought doesn't exist
                    print("Line {} of file {} not found".format(find_line_int, file_str))
                    input_file.close()
                    exit()
            except ValueError:
                print("Line", find_line_str, "isn't a legal line number.")
    except IOError:
        print("The file", file_str, "doesn't exist.")
