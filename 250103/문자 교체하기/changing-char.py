s1, s2 = input().split()
s1 = list(s1)
s2 = list(s2)
s2[0], s2[1] = s1[0], s1[1]

s2 = ''.join(s2)
print(s2)