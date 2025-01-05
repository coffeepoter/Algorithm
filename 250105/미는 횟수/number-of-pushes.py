A = input()
B = input()
cnt = 0
while A != B:
    if cnt == len(A):
        break
    A = A[-1] + A[:-1]
    cnt += 1
if cnt == len(A):
    print(-1)
else:
    print(cnt)