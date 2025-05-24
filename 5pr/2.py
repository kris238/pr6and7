def process_array(arr):
    positive_sum = sum(x for x in arr if x > 0)
    minn = arr.index(min(arr))
    maxx = arr.index(max(arr))
    if minn > maxx:
        minn, maxx = maxx, minn
    product = 1
    for x in arr[minn + 1:maxx]:
        product *= x
    return positive_sum, product
numbers = [3, -1, 6, 1, 3, -3, 5, 0, -2]
result = process_array(numbers)
print("Сумма:", result[0])
print("Произведение:", result[1])
