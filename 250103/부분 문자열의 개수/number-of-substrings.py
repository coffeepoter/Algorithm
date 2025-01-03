A = input()
B = input()
cnt = 0 
for i in range(len(A)):
    if B in A[i:i+2]:
        cnt += 1
print(cnt)