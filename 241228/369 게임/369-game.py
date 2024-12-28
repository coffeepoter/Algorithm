n = int(input())

for i in range(1, n+1):
    digits = [int(d) for d in str(i)]
    if i < 10 and i % 3 == 0 :
        print(0, end=" ")
    elif i > 10 and (digits[0] % 3 == 0 or digits[1] % 3 == 0 or i % 3 == 0):
        print(0, end=" ")
    else:
        print(i, end=" ")
    