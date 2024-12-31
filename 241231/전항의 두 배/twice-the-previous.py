arr = list(map(int, input().split()))
a, b = arr[0], arr[1]
cnt = 2
print(a, end=" ")
print(b, end=" ")

while cnt != 10:
    c = 2 * a + b
    cnt += 1
    print(c, end=" ")
    a, b = b, c
