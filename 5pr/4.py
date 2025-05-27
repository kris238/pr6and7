string = input("Введите строку: ")
if string.startswith("abc"):
    string1 = string.replace("abc", "www", 1)
else:
    string1 = string + "zzz"
print(string1)
