# Print an n digit number in reverse order

num = int(input(" Enter a number : "))
i = 0
print(" Reverse order is : ", end=" ")
while int(num) != 0:
    i = num % 10
    print(int(i), end="")
    num = int(num) / 10
