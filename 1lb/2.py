candidates = [2, 5, 2, 1, 2]
target = 5
candidates.sort()
results = []
combination = []
def bt(start, target):
    if target == 0:
        results.append(list(combination))
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        if candidates[i] > target:
            break
        combination.append(candidates[i])
        bt(i + 1, target - candidates[i])
        combination.pop()
bt(0, target)
print(results)