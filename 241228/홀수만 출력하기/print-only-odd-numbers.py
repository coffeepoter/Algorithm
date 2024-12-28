n = int(input())
num = [int(input()) for _ in range(n)]

for i in range(0,n):
    if num[i] % 3 == 0:
        print(num[i])