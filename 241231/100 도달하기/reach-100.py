n = int(input())
a, b = 1, n

print(a, end=" ")
print(b, end=" ")

while 1:
    c = a + b
    print(c, end=" ")
    if c > 100:
        break
    a, b = b,c