# Write a program to demonstrate EH in python for handling two exceptions, namely, IndexError: list index out of range and ZeroDivisionError.

# import sys
# ch = 0
# while ch != 2:
#     ch = int(input('\n1.Input\t\t2.Exit\nEnter your choice : '))
#     if ch == 1:
#         i = int(input('Enter Index : '))
#         try:
#             my_list = [3, 7, 9, 4, 6]
#             print(my_list[i])
#         except IndexError as e:
#             print(e)


def index():
    ch = 0
    while ch != 2:
        ch = int(input('1.Input\t\t2.Exit\nEnter your choice : '))
        if ch == 1:
            i = int(input('Enter Index : '))
            try:
                my_list = [3, 7, 9, 4, 6]
                print(my_list[i])
            except IndexError as e:
                print(e, "\n")


def zero():
    ch = 0
    while ch != 2:
        ch = int(input('1.Input\t\t2.Exit\nEnter your choice : '))
        if ch == 1:
            a = int(input('Enter First No. : '))
            b = int(input('Enter Second No. : '))
            try:
                i = a / b
                print('division : ', i)
            except ZeroDivisionError as e:
                print(e, "\n")


print("IndexError")
index()
print("\nZeroError")
zero()
