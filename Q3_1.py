# Find the factorial of a given number

def fact(num):
    i = 1
    n = num
    while num != 0:
        i = i * num
        num = num - 1
    print("\nFactorial of ", n, ' is ', i)


num = int(input('Enter a Number : '))
fact(num)
