arr = list(map(int, input().split()))
max_val = -1000
min_val = 1000

for elem in arr:
    if elem == 999 or elem == -999:
        break
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val = elem

print(max_val, min_val)