s = list(input())
s[1] = s[-2] = 'a'
s = ''.join(s)
print(s)