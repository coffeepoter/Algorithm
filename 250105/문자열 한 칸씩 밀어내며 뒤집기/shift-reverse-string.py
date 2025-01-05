s, q = input().split()
q = int(q)
for _ in range(q):
    query = int(input())
    if len(s) > 2:
        if query == 1:
            s = s[1:] + s[0]
            print(s)
        elif query == 2:
            s = s[-1] + s[:-1]
            print(s)
        elif query == 3:
            arr = list(s)
            arr.reverse()
            s = "".join(arr)
            print(s)
    else:
        arr = list(s)
        arr.reverse()
        s = "".join(arr)
        print(s)
