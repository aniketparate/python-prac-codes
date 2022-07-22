# Print Fibonacci series up to n numbers

num = int(input(" Enter a number : "))
i = 2
a = 0
b = 1
print('Fibonacci series : ', a, b, '', end='')
while i < num:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i = i + 1