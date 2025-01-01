arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

for elem in arr:
    print(sum(elem))