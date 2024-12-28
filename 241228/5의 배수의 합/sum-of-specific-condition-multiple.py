n = input().split()
a, b = int(n[0]), int(n[1])
sum = 0

if b >= a:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum += i
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum += i

print(sum)