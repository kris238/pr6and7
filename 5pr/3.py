import random
def c_array(size):
    even_numbers = set()
    while len(even_numbers) < size:
        num = random.randint(1, 100)
        if num % 2 == 0:
            even_numbers.add(num)
    even_array = sorted(even_numbers)
    return even_array
size = int(input("Введите размер массива:"))
even_array = c_array(size)
print(even_array)
