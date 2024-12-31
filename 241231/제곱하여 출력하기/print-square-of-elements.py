n = int(input())
arr = list(map(int, input().split()))

arr = [elem ** 2 for elem in arr]

for elem in arr:
    print(elem, end=" ")