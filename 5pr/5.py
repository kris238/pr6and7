def cal(a, b):
    r = (a + 4 * b) * (a - 3 * b) + a ** 2
    return r
a = float(input("Введите значение a:"))
b = float(input("Введите значение b:"))
r = cal(a, b)
print("Результат выражения:", r)
