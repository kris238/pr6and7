s = [-5, -10, 3, -2, 8, -1, 4, -7]
f_positive = None
l_negative = None
for num in s:
    if num > 0 and f_positive is None:
        f_positive = num
    if num < 0:
        l_negative = num
if f_positive is not None:
    print(f"Первый положительный элемент: {f_positive}")
else:
    print("Положительных элементов нет.")
if l_negative is not None:
    print(f"Последний отрицательный элемент: {l_negative}")
else:
    print("Отрицательных элементов нет.")