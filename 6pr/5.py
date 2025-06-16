C = input('Введите символ:')
A = ['abac', 'banana', 'apple', 'abra', 'a', 'axa']
count = 0
for element in A:
    if len(element) > 1 and element[0] == C and element[-1] == C:
        count += 1
print(f"Количество элементов, начинающихся на '{C}': {count}")