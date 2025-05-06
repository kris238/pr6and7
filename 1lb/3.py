nums = [1, 2, 3, 1]
e_s = set()
duplicates = False
for num in nums:
    if num in e_s:
        duplicates = True
        break
    e_s.add(num)
print(duplicates)  # Вывод: True
