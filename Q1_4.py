# Print all the numbers between 100 to 200 which are divisible by 4 and 7

i = 100
print(" Number from 100 to 200 divisible by 4 and 7 are : ", end=" ")
while i <= 200:
    if i % 4 == 0 and i % 7 == 0:
        print(i, end=" ")
    else:
        pass
    i = i + 1