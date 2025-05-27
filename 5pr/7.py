def is_point_in_circle(x, y, r):
    return x**2 + y**2 <= r**2
x = int(input("x = "))
y = int(input("y = "))
radius = int(input("Введите радиус окружности:"))
if is_point_in_circle(x, y, radius):
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")
