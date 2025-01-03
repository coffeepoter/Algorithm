s = list(input())
m, n = s[0], s[1]

for i in range(len(s)):
    if s[i] == m:
        s[i] = n
    elif s[i] == n:
        s[i] = m

s = ''.join(s)
print(s)
    