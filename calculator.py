"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    choice = input("Enter your equation >> ")
    token = choice.split(' ')

    if token[0] == 'q':
        print("You will exit.")
        break
    else:
        print("Will continue tomorrow.")