a = input().split()
b = input().split()
c = input().split()
a1, a2 = a[0], int(a[1])
b1, b2 = b[0], int(b[1])
c1, c2 = c[0], int(c[1])

if a1 == "Y" and b1 == "Y":
    if a2 >= 37 and b2 >= 37:
        print("E")
    else:
        print("N")
elif a1 == "Y" and c1 == "Y":
    if a2 >= 37 and c2 >=37:
        print("E")
    else:
        print("N")
elif b1 == "Y" and c1 == "Y":
    if b2 >= 37 and c2 >=37:
        print("E")
    else:
        print("N")
elif a1 == "Y" and b1 == "Y" and c1 == "Y":
    if (a2 >=37 and b2 >= 37) or (a2 >=37 and c2 >= 37) or (b2 >=37 and c2 >= 37):
        print("E")
    else:
        print("N")
else:
    print("N")
