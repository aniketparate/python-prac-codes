# Find number of list elements of different data types

def dataType(list):
    for element in list:
        if isinstance(element, int):
            print(" ", element, " is an integer\n")
        elif isinstance(element, str):
            print(" ", element, " is an string\n")
        elif isinstance(element, float):
            print(" ", element, " is an float number")


a_list = [10, 'Flame', 16.91]
print(" ", a_list, "\n")
dataType(a_list)
