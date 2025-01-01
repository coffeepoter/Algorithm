arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for elem in arr:
    ans = sum(elem)/len(elem)
    print(f"{ans:.1f}", end= " ")
print()

for i in range(4):
    ans = (arr[0][i] + arr[1][i]) / 2
    print(f"{ans:.1f}", end=" ")
print()

sum_val = 0
for elem in arr:
    sum_val += sum(elem)
ans = sum_val / 8
print(f"{ans:.1f}")