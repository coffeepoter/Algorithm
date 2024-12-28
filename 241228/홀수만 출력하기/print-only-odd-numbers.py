n = int(input())
num = [int(input()) for _ in range(n)]

for i in range(0,n):
    if num[i] % 3 == 0 and num[i] % 2 == 1:
        print(num[i])