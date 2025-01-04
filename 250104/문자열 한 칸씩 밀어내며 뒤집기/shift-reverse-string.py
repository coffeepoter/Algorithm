s, q = input().split()
q = int(q)
for _ in range(q):
    query = int(input())
    if query == 1:
        s = s[1:] + s[0]
        print(s)
    elif query == 2:
        s = s[-1] + s[:-1]
        print(s)
    elif query == 3:
        s = list(s)
        s.reverse()
        print("".join(s))
        
