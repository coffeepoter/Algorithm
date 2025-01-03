s = list(input())
s = [s[0] if ch == s[1] else ch for ch in s]
print("".join(s))