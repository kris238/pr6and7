Jw = "ab"
St = "aabbccd"
jewels = set(Jw)
count = 0
for stone in St:
    if stone in jewels:
        count += 1
print(count)