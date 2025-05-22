array = []
for i in range(14):
    num = int(input())
    array.append(num)
array.append(sum(array))
for i in array:
    print(i, end=" ")


