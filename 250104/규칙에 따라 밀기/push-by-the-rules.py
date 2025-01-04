A = input()
order = input()
for elem in order:
    if elem == 'L':
        A = A[1:] + A[0]
    elif elem == 'R':
        A = A[-1] + A[:-1]
print(A)
