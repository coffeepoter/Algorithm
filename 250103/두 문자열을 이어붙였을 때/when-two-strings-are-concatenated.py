A = input()
B = input()
s1 = A + B
s2 = B + A
same = False
for i in range(len(A+B)):
    if s1[i] != s2[i]:
        break
    else:
        same = True

if same:
    print("true")
else:
    print("false")