def ZerosToEnd(array, n):
    count=0
    for i in range(n):
        if array[i] != 0:
            array[count] = array[i]
            count += 1

    while count < n:
        array[count] = 0
        count += 1
array = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
for ar in array:
    if ar != 0:
        array.sort()
n = len(array)
ZerosToEnd(array, n)


print("Array after sorting and pushing all zeros to end of array:")
print(array)