# Display odd and even numbers between a given range

i = 0
num = int(input(" Enter a number : "))
print(" Even numbers are : ", end=" ")
while i < num:
    print(i, end=" ")
    i = i + 2

i = 0
print("\n Odd numbers are : ", end=" ")
while i < num:
    print(i + 1, end=" ")
    i = i + 2