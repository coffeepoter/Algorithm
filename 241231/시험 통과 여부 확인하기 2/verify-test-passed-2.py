n = int(input())
cnt = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    sum_val = 0
    for ele in arr:
        sum_val += ele
    avg = sum_val / 4
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")     
print(cnt)