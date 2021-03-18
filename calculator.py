"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    choice = input("Enter your equation >> ")
    token = choice.split(' ')
    new_list = []

    for index in token[1:]:
        index = float(index)
        new_list.append(index)

    if token[0] == 'q':
        print("You will exit.")
        break

    
    elif token[0] == "+":
        result = new_list[0] + new_list[1]
    elif token[0] == "-":
        result = token[0] + token[1]
    else:
            print("Not valid, try again.")
    print(result)