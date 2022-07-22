# Check the presence/absence of a given value in the list; then display the total number of occurrences and index of the position of each occurrence

def countOccurrences(arr, n, num):
    count = 0
    for i in range(n):
        if num == arr[i]:
            pos.append(i)
            count = count + 1
        else:
            pass
    return count


arr = [5, 7, 5, 1, 1, 5, 2, 7, 5, 10, 5, 2, 3, 5, 7, 10]
pos = []
print(arr)
n = len(arr)
num = int(input('Enter No to be searched : '))
print(num, ' is found ', countOccurrences(arr, n, num), ' times')
print(num, ' occurs at position ', pos)
