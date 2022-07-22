# Sort list elements; press 1 for ascending order and, press 2 for descending order (choice based)

list = [12, 7, 2, 16, 4, 5, 34, 15, 21, 18, 9, 41, 25, 1]
ch = 0
while ch != 3:
    ch = int(input("Press 1 for Ascending \nPress 2 for Descending and \nPress 3 for Exit\nEnter your choice here : "))
    if ch == 1:
        list.sort(reverse=False)
        print('\nAscending Sorted list : ', list, "\n")
    elif ch == 2:
        list.sort(reverse=True)
        print('\nDescending Sorted list : ', list, "\n")
    else:
        exit(0)

