s, q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    query = input().split()
    n = int(query[0])

    if n == 1:
        a, b = int(query[1]) - 1, int(query[2]) - 1
        s[a], s[b] = s[b], s[a]
    elif n == 2:
        a, b = query[1], query[2]
        s = [b if ch == a else ch for ch in s]
    print("".join(s))
