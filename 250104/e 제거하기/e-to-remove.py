s = input()

if 'e' in s:
    idx = s.index('e')
    print(s[:idx]+s[idx+1:])